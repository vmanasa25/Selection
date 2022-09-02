import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.orig_image = image.load("Assets/hand.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        self.image_smaller = image.load("Assets/hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False



    def follow_mouse(self): 
        self.rect.center = pygame.mouse.get_pos()

    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)


    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")

        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def on_rect(self, rects): # return a list with all rectangles that collide with the hand hitbox
        return [rectangle for rectangle in rects if self.rect.colliderect(rectangle.rect)]


    def select_rects(self, rects, score): # will select rectangles that collide with the hand gesture is made
        if self.left_click: #if gesture
            for rectangle in self.on_rect(rects):
                score += 50
        else:
            self.left_click = False

        return score


    def select_rects_new(self, rects, score): # will select all rectangles 
        for rectangle in self.on_rect(rects):
            rect_score = rectangle.kill(rects)
            score += 1000

        return score
