import tkinter as tk
from tkinter import messagebox



class Board:
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        return False

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def check_win(self, player):
        s = player.symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")  
        self.root.geometry("400x200")  

        
        self.player_a = BoardPlayer(1)
        self.player_b = BoardPlayer(-1)
        self.active_player = self.player_a
        self.rounds_played = 0
        self.player_a_score = 0
        self.player_b_score = 0

        self.create_start_screen()

    def create_start_screen(self):
        self.start_frame = tk.Frame(self.root, width=500, height=300)
        self.start_frame.pack()

        self.rounds_label = tk.Label(self.start_frame, text=f"Rounds Played: {self.rounds_played}")
        self.rounds_label.pack()
        
        self.rules = tk.Label(self.start_frame, text=f"RULES \n [X] Starts to mark the grid. \n The winner starts the new round.")
        self.rules.pack()

        self.player_a_score_label = tk.Label(self.start_frame, text=f"Player [X] Score: {self.player_a_score}")
        self.player_a_score_label.place(x=10, y=200)
        self.player_a_score_label.pack(side="left")

        self.player_b_score_label = tk.Label(self.start_frame, text=f"Player [O] Score: {self.player_b_score}")
        self.player_b_score_label.pack(side="right")

        self.start_button = tk.Button(self.start_frame, text="Start Game", command=self.start_game, bg="green", font="bold", border="2px solid black", justify="center", padx="5")
        self.start_button.place(x="100", y="100")
        self.start_button.pack()

    def start_game(self):
        self.start_frame.destroy()

        self.board = Board()
        self.buttons = []

        self.create_board()
        self.rounds_played += 1
        self.rounds_label.config(text=f"Rounds Played: {self.rounds_played}")

    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.board_frame, text='', font=('Arial', 30), width=3, height=1,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.back_button = tk.Button(self.board_frame, text="Back to Start", command=self.back_to_start)
        self.back_button.grid(row=3, column=0, columnspan=3)

    def handle_click(self, row, col):
        cell = row * 3 + col
        if self.board.make_turn(cell, self.active_player):
            self.buttons[row][col].config(text=self.board.sign_to_printable(self.active_player.symbol))
            if self.board.check_win(self.active_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.active_player.symbol} wins!")
                if self.active_player == self.player_a:
                    self.player_a_score += 1
                    self.player_a_score_label.config(text=f"Player A Score: {self.player_a_score}")
                else:
                    self.player_b_score += 1
                    self.player_b_score_label.config(text=f"Player B Score: {self.player_b_score}")
                self.reset_board()
            elif self.board.is_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.toggle_player()
        else:
            messagebox.showerror("Tic Tac Toe", "Invalid Move")

    def toggle_player(self):
        self.active_player = self.player_b if self.active_player == self.player_a else self.player_a

    def reset_board(self):
        self.board_frame.destroy()
        self.create_start_screen()

    def back_to_start(self):
        self.board_frame.destroy()
        self.create_start_screen()

class BoardPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

def start_game():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_game()
