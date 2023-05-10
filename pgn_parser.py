"""
Auteur: Mathis & Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : pgn_parser
Contacts:
mathis.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""

from pgn_lexer import *
from pgn_ast import *
from pgn_visitor import *

"""
Dans ce fichier on va réaliser le parsage du fichier pgn en entrée.
La fonction parse_game permet d'analyser tour à tour les tokens renvoyés par le lexer, et nous renvoie vers la fonction parse_move si le token est le numero d'un tour.
Note à nous même : pour l'instant on affiche pas toutes les indications avant la partie du style la date le site etc. A voir si on peut en faire qq chose sur l'interface graphique.
"""

class PgnParser:
    def __init__(self):
        self.current_token = None
        self.token_index = -1
        self.tokens = []

    def parse(self, tokens):
        self.tokens = tokens
        self.token_index = -1
        self.current_token = None
        self.advance()
        return self.parse_game()

    def parse_game(self):
        moves = []
        results = []
        while self.current_token is not None:
            if self.current_token.name == "NUMBER":
                move_number, move_white, move_black = self.parse_move()
                moves.append(MoveNode(move_number, move_white, move_black))
            elif self.current_token is not None and self.current_token.name == "RESULT":
                result = self.current_token.value
                results.append(ResultNode(result))
            self.advance()
        return GameNode(moves, results)

    def parse_move(self):
        move_number = self.current_token.value[:-1]
        self.advance()
        move_white = self.parse_single_move()
        self.advance()
        if self.current_token is None or self.current_token.name == "RESULT":
            move_black = None
        else:
            move_black = self.parse_single_move()
        return move_number, move_white, move_black

    def parse_single_move(self):
        if self.current_token is None:
            return None
        move = self.current_token.value
        return move

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None
