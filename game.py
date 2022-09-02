import pygame
import time
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from rectangle import Rectangle
import cv2
import ui
import numpy as np 
from scipy.stats.stats import pearsonr   


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.rectlist = []
        # Load camera
        self.cap = cv2.VideoCapture(0)


    def reset(self): 
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.rectangles = []
        self.rectangles_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()




    def spawn_rectangles(self): #spawns rectangles

        if self.time_left > GAME_DURATION - 0.4:
            self.rectangles.append(Rectangle())

    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)
        #Obtaining x,y coordinates of hand center
        COORDINATES_HAND.append(self.hand.rect.center) 
        if len(COORDINATES_HAND) == 101:
            COORDINATES_HAND.pop(0)
        return COORDINATES_HAND

    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the rectangles
        for i in self.rectangles:
            self.rectlist = i.draw(self.surface)
        # draw the hand
        self.hand.draw(self.surface)
        # draw the score
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        # draw the time left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        return self.rectlist


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)


    def update(self):

        self.load_camera()
        new = np.array(self.set_hand_position())

        self.game_time_update()
    
        newone =  np.array(self.draw())

        if self.time_left > 0:
            self.spawn_rectangles()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            
            for i in self.rectangles:
                i.move()

        else: # when the game is over
            if ui.button(self.surface, 540, "Continue"):
                return "menu", new, newone

        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
        return None, new, newone


    def calc(self): #Calculation of correlation coefficient
        
        status, returned, returnedone = self.update()
        if (len(returned) == len(returnedone)) and (len(returned)!=0 and len(returnedone)!=0):
            corr_x = pearsonr(returned[:,0], returnedone[:,0])
            corr_y = pearsonr(returned[:,1], returnedone[:,1])
            correl = (corr_x[0] + corr_y[0])/2
            print(correl)
            self.score = self.hand.select_rects(self.rectangles, self.score)
            if correl > 0.90:
                self.score = self.score + 1
            if correl > 0.98:
                self.score = self.hand.select_rects_new(self.rectangles, self.score)
    

