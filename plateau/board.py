import pygame 
from .pieces import *
from .constants import *

class newBoard : 
    def __init__(self, Width, Height, Rows, Col, Square, Win):
        self.Width = Width
        self.Height = Height
        self.Rows = Rows
        self.Col = Col
        self.Square = Square
        self.Win = Win
        self.Board = []
        self.create_board()
    
    def __create_board(self):
        for row in range (self.Rows):
            self.Board.append([0 for i in range(self.Cols)])
            for col in range (self.Cols):
                pass