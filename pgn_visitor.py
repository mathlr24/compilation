"""
Auteur: Mathis & Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : pgn_visitor
Contacts:
mathis.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""

class PgnVisitor:
    def __init__(self):
        self.moves = []

    def visit_game(self, node):
        for move in node.moves:
            move.accept(self)

    def visit_move(self, node):
        if node.move_white:
            self.moves.append(node.move_white)
        if node.move_black:
            self.moves.append(node.move_black)
