import pygame
from constants import *


pygame.init()

clock = pygame.time.Clock()

win = pygame.display.set_mode((width, height))

def get_position(x,y):
    row = y//square
    col = x//square

def main():
    run = True
    FPS = 60

    while run :
        clock.tick(FPS)
        win.blit(white_bishop, (50, 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE and game_over:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if pygame.mouse.get_pressed()[0]:
                    location = pygame.mouse.get_pos()
                    


main ()
