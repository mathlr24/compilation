from pgn_lexer import PgnLexer
from pgn_parser import PgnParser
from pgn_visitor import *
from pgn_interface import *
from utils import convert_moves
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py fichier.pgn")
    sys.exit()

nom_fichier = sys.argv[1]

# Traitement du fichier
with open(nom_fichier, 'r') as fichier:
    # Lire le contenu du fichier et faire quelque chose avec
    contenu = fichier.read()


# Analyse lexicale
lexer = PgnLexer()
tokens = lexer.tokenize(contenu)
print("==== Tokens ====")
print(tokens)

# Analyse syntaxique
parser = PgnParser()
ast = parser.parse(tokens)
print("==== AST ====")
print(ast)

# Création de la partie d'échecs
visitor = PgnVisitor()
ast.accept(visitor)
moves = visitor.moves
new_moves = []
for move in moves:
    if move == "OO":
        move = move.replace("OO","O-O")
        new_moves.append(move)
    else:
        new_moves.append(move)
print(new_moves)
new_moves = convert_moves(new_moves)
white_moves = new_moves[::2]
black_moves = new_moves[1::2]
game = ChessGame(white_moves, black_moves)
root=tk.Tk()
board = ChessBoard(root, game)
board.pack()
root.mainloop()

print("==== Chess Game ====")
print(game)