import pygame
import random
import time
import image
from settings import *
import math 


class Rectangle:
    def __init__(self):
        #size
        random_size_value = random.uniform(RECTANGLE_SIZE_RANDOMIZE[0], RECTANGLE_SIZE_RANDOMIZE[1])
        size = (int(RECTANGLE_SIZES[0] * random_size_value), int(RECTANGLE_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load("Assets/rectangle.png", size=size, flip=moving_direction=="circle")]
        self.current_frame = 0
        self.animation_timer = 0



    def define_spawn_pos(self, size): # define the start pos and moving vel of the rectangle

        vel = random.uniform(RECTANGLE_MOVE_SPEED["min"], RECTANGLE_MOVE_SPEED["max"])
        moving_direction = "circle"
        if moving_direction == "circle":
            start_pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            self.vel = [-vel, vel]  
        return moving_direction, start_pos


    def move(self):

        next_point = [15* math.cos(self.vel[0]), 15* math.sin(self.vel[0])]
        self.rect.move_ip(next_point)
        self.vel = [x+0.07 for x in self.vel]
        


    def animate(self): # change the frame of the rectangle when needed
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0


    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rectangles)


    def draw(self, surface):
        self.animate()
        #Obtaining x,y coordinates of Rectangle center
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")

        COORDINATES_RECTANGLE.append(self.rect.center) 
        if len(COORDINATES_RECTANGLE) == 101:
            COORDINATES_RECTANGLE.pop(0)
        return COORDINATES_RECTANGLE


    
    def kill(self, rectangles): # remove the rectangle from the list
        rectangles.remove(self)
        return 1


