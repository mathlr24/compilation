import pygame
import os

width, height = 760,760
rows, cols = 8,8
square = width // rows


#Colors
brown = (88, 41, 0)
white = (112, 114, 110)

path = "chess_images"

#Black piecies
black_Knight = pygame.transform.scale(pygame.image.load(os.path.join(path, "bKN.png")), (square, square))
black_bishop = pygame.transform.scale(pygame.image.load(os.path.join(path, "bB.png")), (square, square))
black_King = pygame.transform.scale(pygame.image.load(os.path.join(path, "bK.png")), (square, square))
black_pawn = pygame.transform.scale(pygame.image.load(os.path.join(path, "bP.png")), (square, square))
black_Queen = pygame.transform.scale(pygame.image.load(os.path.join(path, "bQ.png")), (square, square))
black_Rook = pygame.transform.scale(pygame.image.load(os.path.join(path, "bR.png")), (square, square))

#White piecies
white_Knight = pygame.transform.scale(pygame.image.load(os.path.join(path, "wKN.png")), (square, square))
white_bishop = pygame.transform.scale(pygame.image.load(os.path.join(path, "wB.png")), (square, square))
white_King = pygame.transform.scale(pygame.image.load(os.path.join(path, "wK.png")), (square, square))
white_pawn = pygame.transform.scale(pygame.image.load(os.path.join(path, "wP.png")), (square, square))
white_Queen = pygame.transform.scale(pygame.image.load(os.path.join(path, "wQ.png")), (square, square))
white_Rook = pygame.transform.scale(pygame.image.load(os.path.join(path, "wR.png")), (square, square))