from cmath import cos, sin
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
        # self.mainClock = pygame.time.Clock()
        self.animation_timer = 0

        



    def define_spawn_pos(self, size): # define the start pos and moving vel of the rectangle
        vel = random.uniform(RECTANGLE_MOVE_SPEED["min"], RECTANGLE_MOVE_SPEED["max"])
        #vel = random.uniform(RECTANGLE_MOVE_SPEED["min"], RECTANGLE_MOVE_SPEED["max"])
        t = pygame.time.Clock().tick(FPS)/50
        # print(t)
        # print(t)
        radius = 3
        # print(t)
        # moving_direction = random.choice(("right","left"))
        #t = self.current_frame / vel
        moving_direction = "circle"
        # if moving_direction == "right":
        #     start_pos = (SCREEN_WIDTH - size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
        #     #print(start_pos)
        #     self.vel = [-vel, vel]
        # if moving_direction == "left":
        #     start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT+size[1]))
        #     #print(start_pos)
        #     self.vel = [-vel, vel]
        if moving_direction == "circle":
            # print(t)
            start_pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            # print(start_pos)
            # self.vel = [radius*np.sin(t), -radius*np.cos(t)]
            self.vel = [-vel, vel]  
            # self.vel = [math.pi(t+1), -math.pi(t)]
            # print(self.vel)       
            # print(vel)
            #print(start_pos)
        # if moving_direction == "up":
        #     start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
        #     #print(start_pos)
        #     self.vel = [vel, -vel]
        # if moving_direction == "down":
        #     start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
        #     #print(start_pos)
        #     self.vel = [-vel, vel]
        # if moving_direction == "round":
        #     start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
        #     self.vel = [vel, 0]
        #     self.x_new = RECTANGLE_MOVE_POINT_X*math.cos(RECTANGLE_ANGLE)+500
        #     self.y_new = RECTANGLE_MOVE_POINT_X*math.sin(RECTANGLE_ANGLE)+300
        #     image.draw.rect(surface,"green",(self.x_new, self.y_new), 1)
            # angle1 += 0.002
        return moving_direction, start_pos


    def move(self):
        # self.rect.move_ip(self.vel)
        # print([3*math.sin(x) for x in self.vel])

        next_point = [15* math.cos(self.vel[0]), 15* math.sin(self.vel[0])]
        self.rect.move_ip(next_point)
        self.vel = [x+0.07 for x in self.vel]
        # print(self.vel)
        


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
        # print(COORDINATES_RECTANGLE)
        return COORDINATES_RECTANGLE
        # if DRAW_HITBOX:
        #     self.draw_hitbox(surface)

    
    def kill(self, rectangles): # remove the rectangle from the list
        rectangles.remove(self)
        return 1


