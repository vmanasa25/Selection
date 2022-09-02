import pygame
import numpy as np

WINDOW_NAME = "Selection Game"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
dx, dy = 1, 2
FPS = 60
DRAW_FPS = False

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
RECTANGLE_SIZES = (50, 38)
RECTANGLE_SIZE_RANDOMIZE = (1,2) # for each new rectangle, it will multiply the size with an random value beteewn 1 and 2

COORDINATES_RECTANGLE = []
COORDINATES_HAND = []
returned = np.arange(200).reshape(100,2)
returnedone = np.arange(200).reshape(100,2)

# drawing
DRAW_HITBOX = False # will draw all the hitboxes

# animation
ANIMATION_SPEED = 0.08 # the frame of the rectangles will change 

# difficulty
GAME_DURATION = 30 
RECTANGLE_SPAWN_TIME = 0
RECTANGLE_MOVE_SPEED = {"min": 1, "max": 2}

# colors
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} # second is the color when the mouse is on the button


# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
