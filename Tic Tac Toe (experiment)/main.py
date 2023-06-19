import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.score = {"X": 0, "O": 0}

        self.score_label = tk.Label(
            self.root, text="Score: X: 0  O: 0", font=("Arial", 16), pady=10
        )
        self.score_label.grid(row=0, columnspan=3)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.root,
                    text=" ",
                    font=("Arial", 20),
                    width=6,
                    height=3,
                    command=lambda r=row, c=col: self.make_move(r, c),
                )
                self.buttons[row][col].grid(row=row + 1, column=col)

        self.restart_game()

    def restart_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", state=tk.NORMAL)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner():
                self.update_score()
                self.game_over()
            elif self.is_board_full():
                self.game_over(tie=True)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.root.after(500, self.computer_move)

    def computer_move(self):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    available_moves.append((row, col))

        if available_moves:
            row, col = random.choice(available_moves)
            self.make_move(row, col)

    def check_winner(self):
        # Check rows
        for row in range(3):
            if (
                self.board[row][0] == self.board[row][1]
                == self.board[row][2]
                != " "
            ):
                return True

        # Check columns
        for col in range(3):
            if (
                self.board[0][col] == self.board[1][col]
                == self.board[2][col]
                != " "
            ):
                return True

        # Check diagonals
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] != " "
            or self.board[0][2] == self.board[1][1] == self.board[2][0] != " "
        ):
            return True

        return False

    def is_board_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return False
        return True

    def update_score(self):
        self.score[self.current_player] += 1
        self.score_label.config(
            text=f"Score: X - {self.score['X']}  O - {self.score['O']}"
        )

    def game_over(self, tie=False):
        if tie:
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            winner = "X" if self.current_player == "X" else "O"
            messagebox.showinfo("Game Over", f"{winner} wins!")

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

        choice = messagebox.askyesno("Game Over", "Do you want to play again?")
        if choice:
            self.restart_game()
        else:
            self.root.destroy()

    def start(self):
        self.root.mainloop()


game = TicTacToe()
game.start()