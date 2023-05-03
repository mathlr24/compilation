import pygame
from .constants import *

class Piece:
    def __init__(self,Square, image, color, row, col):
        self.Square = Square
        self.image = image 
        self.color = color
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0 

    def piece_move(self, row, col):
        self.row = row
        self.col = col 
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col*self.Square
        self.x = self.row*self.Square

class Pawn(Piece):
    def __init__(self, Square, image, color, type, row, col):
        super.__init__(Square, image, color, type, row, col)
        