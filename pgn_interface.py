import chess
import tkinter as tk

class Board:
    def __init__(self):
        self.board = chess.Board()

    def parse_move(self, move):
        x1, y1 = move.from_square % 8, move.from_square // 8
        x2, y2 = move.to_square % 8, move.to_square // 8
        return (x1, y1, x2, y2)

class ChessGame:
    def __init__(self, white_moves, black_moves):
        self.board = Board()
        self.white_moves = [self.board.parse_move(move) for move in white_moves]
        self.black_moves = [self.board.parse_move(move) for move in black_moves]
        self.current_move = 0

    def make_move(self, move):
        player_moves = self.white_moves if self.get_current_player() == 'white' else self.black_moves

        if move not in player_moves:
            print("Invalid move:", move)
            return

        x1, y1, x2, y2 = move
        piece = self.board.board.piece_at(chess.square(x1, 7 - y1))
        self.board.board.remove_piece_at(chess.square(x1, 7 - y1))
        self.board.board.set_piece_at(chess.square(x2, 7 - y2), piece)
        self.current_move += 1
    
    def make_previous_move(self, move):
        player_moves = self.white_moves if self.get_current_player() == 'white' else self.black_moves

        if move not in player_moves:
            print("Invalid move:", move)
            return

        x1, y1, x2, y2 = move
        piece = self.board.board.piece_at(chess.square(x1, 7 - y1))
        self.board.board.remove_piece_at(chess.square(x1, 7 - y1))
        self.board.board.set_piece_at(chess.square(x2, 7 - y2), piece)
        self.current_move -= 1

    def get_board(self):
        rows = []
        for i in range(8):
            row = []
            for j in range(8):
                piece = self.board.board.piece_at(chess.square(j, 7 - i))
                if piece:
                    row.append(piece.symbol())
                else:
                    row.append(' ')
            rows.append(row)
        return rows

    def get_current_player(self):
        return 'white' if self.current_move % 2 == 0 else 'black'

    def is_game_over(self):
        return self.board.board.is_game_over()

    def get_moves(self):
        return self.white_moves + self.black_moves

class ChessBoard(tk.Frame):
    def __init__(self, parent, game):
        tk.Frame.__init__(self, parent, width=400, height=400)
        self.parent = parent
        self.game = game
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.draw_pieces()
        self.current_player = 'white'
        self.next_button = tk.Button(self.parent, text="Suivant", command=self.next_move)
        self.previous_button = tk.Button(self.parent, text="Precedent", command=self.previous_move)
        self.next_button.pack(side="right")
        self.previous_button.pack(side="right")
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = 'white' if (i + j) % 2 == 0 else 'gray'
                x1, y1 = j * 50, i * 50
                x2, y2 = (j + 1) * 50, (i + 1) * 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_pieces(self):
        pieces = self.game.get_board()
        for i in range(8):
            for j in range(8):
                piece = pieces[i][j]
                if piece != '.':
                    x, y = j * 50 + 25, i * 50 + 25
                    self.canvas.create_text(x, y, text=piece, font=('Arial', 24), tags='piece')

    def on_click(self, event):
        x, y = event.x, event.y
        col, row = x // 50, y // 50
        move = (col, row, col, row)
        current_player = self.game.get_current_player()
        if move in (self.game.white_moves if current_player == 'white' else self.game.black_moves):
            self.game.make_move(move)
            self.canvas.delete('piece')
            self.draw_pieces()
        else:
            print("Invalid move:", move)

    def next_move(self):
        current_player = self.game.get_current_player()
        player_moves = self.game.white_moves if current_player == 'white' else self.game.black_moves
        if self.game.current_move // 2 < len(player_moves):
            move = player_moves[self.game.current_move // 2]
            self.game.make_move(move)
            self.canvas.delete('piece')
            self.draw_pieces()
            self.current_player = self.game.get_current_player()
            if not self.game.is_game_over():
                self.parent.title("Tour des " + self.current_player + "s")
            else:
                self.parent.title("Fin de la partie")

    def previous_move(self):
        current_player = self.game.get_current_player()
        player_moves = self.game.white_moves if current_player == 'white' else self.game.black_moves
        if self.game.current_move // 2 < len(player_moves):
            move = player_moves[self.game.current_move // 2]
            self.game.make_previous_move(move)
            self.canvas.delete('piece')
            self.draw_pieces()
            self.current_player = self.game.get_current_player()
            if not self.game.is_game_over():
                self.parent.title("Tour des " + self.current_player + "s")
            else:
                self.parent.title("Fin de la partie")