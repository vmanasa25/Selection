# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
from settings import *
from menu import Menu
from game import Game

from scipy.stats.stats import pearsonr   

# Setup pygame/window --------------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,32) # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()

# Fonts ----------------------------------------------------------- #
fps_font = pygame.font.SysFont("coopbl", 22)


# Variables ------------------------------------------------------- #
state = "menu"
returnedList = np.arange(200).reshape(100,2)
returnedListOne = np.arange(200).reshape(100,2)

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)

# Functions ------------------------------------------------------ #
def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    global state
    global returnedList
    global returnedListOne
    if state == "menu":
        if menu.update() == "game":
            game.reset() # reset the game to start a new game
            state = "game"
    elif state == "game":
        status, returnedList, returnedListOne = game.update()
        if status == "menu":
            state = "menu"
    pygame.display.update()
    mainClock.tick(FPS)
    return returnedList, returnedListOne



# Loop ------------------------------------------------------------ #
while True:

    # Buttons ----------------------------------------------------- #
    user_events()

    # Update ------------------------------------------------------ #
    returned, returnedone = update()
    # returned = returned[returned>0]
    # returnedone = returnedone[returnedone>0]
    # # print(returned)
    # print(returned)

    if (len(returned) == len(returnedone)) and (len(returned)!=0 and len(returnedone)!=0):
        corr_x = pearsonr(returned[:,0], returnedone[:,0])
        # print(corr_x)
        corr_y = pearsonr(returned[:,1], returnedone[:,1])
        # print(corr_y)
        correl = (corr_x[0] + corr_y[0])/2
        print(correl)
        

    # FPSl
    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255,200,20))
        SCREEN.blit(fps_label, (5,5))
