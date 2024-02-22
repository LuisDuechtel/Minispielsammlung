import tkinter as tk
from tkinter import messagebox
import pygame

class Board:
    def __init__(self):
        self.state = [0] * 9

    def make_turn(self, cell, symbol):
        if self.state[cell] == 0:
            self.state[cell] = symbol
            return True
        return False

    def check_win(self, symbol):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]
        for combo in winning_combinations:
            if all(self.state[i] == symbol for i in combo):
                return True
        return False

    def is_full(self):
        return all(cell != 0 for cell in self.state)

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("1200x800")
        
        self.background_image = tk.PhotoImage(file="assets/vulcan.png")  
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.current_player = 1
        self.board = Board()
        
        self.create_board()

    def create_board(self):
        self.main_frame = tk.Frame(self.root, bg='grey')
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.main_frame, text='', font=('Arial', 30), width=3, height=1,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

    def handle_click(self, row, col):
        cell = row * 3 + col
        if self.board.make_turn(cell, self.current_player):
            self.buttons[cell].config(text='X' if self.current_player == 1 else 'O')
            if self.board.check_win(self.current_player):
                pygame.init()
                pygame.mixer.init()
                sound = pygame.mixer.Sound("assets/drunkensailor.mp3")
                sound.play()
                self.reset_board()
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            elif self.board.is_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            elif self.current_player == 1:
                self.current_player = -1
            else:
                self.current_player = 1               
        else:
            messagebox.error_message("Tic Tac Toe", "Invalid Move")

    def reset_board(self):
        for button in self.buttons:
            button.config(text='')
        self.current_player = 1
        self.board = Board()

def start_game():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_game()
