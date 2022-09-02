import pygame
import image

Screen_Width = 1280
Screen_Height = 720

pygame.display.set_caption("Selector")
Screen = pygame.display.set_mode((Screen_Width, Screen_Height), 0, 32)

bg = image.load("Assets/background.jpg", size = (Screen_Width, Screen_Height), convert="default")

from hand import Hand

hand = Hand()

while True:

    image.draw(Screen, bg, (Screen_Width // 2, Screen_Height // 2), pos_mode="center")

    image.draw(Screen, hand.image, hand.rect, pos_mode="center")

    hand.follow_mouse()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.update()