import tkinter as tk
import random

class HangmanGame:
    def __init__(self):
        self.word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]
        self.word = random.choice(self.word_list)
        self.guessed_letters = []
        self.lives = 7
        self.incorrect_guesses = []
        self.word_so_far = ["_"] * len(self.word)

        self.window = tk.Tk()
        self.window.title("Hangman Game")
        self.window.geometry("400x400")

        self.label = tk.Label(self.window, text=" ".join(self.word_so_far), font=("Arial", 24))
        self.label.pack()

        self.entry = tk.Entry(self.window, font=("Arial", 24))
        self.entry.bind("<Return>", self.guess_letter)
        self.entry.pack()

        self.lives_label = tk.Label(self.window, text=f"Lives: {self.lives}", font=("Arial", 18))
        self.lives_label.pack()

        self.update_word_so_far()

    def guess_letter(self, event):
        letter = self.entry.get().lower()
        if len(letter) == 1 and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter in self.word:
                for i, c in enumerate(self.word):
                    if c == letter:
                        self.word_so_far[i] = letter
                self.update_word_so_far()
                if "_" not in self.word_so_far:
                    self.show_message("Congratulations! You have guessed the word.")
            else:
                self.incorrect_guesses.append(letter)
                self.lives -= 1
                self.lives_label.config(text=f"Lives: {self.lives}")
                if self.lives == 0:
                    self.show_message(f"Game over. The word was {self.word}.")
        self.entry.delete(0, tk.END)

    def update_word_so_far(self):
        self.label.config(text=" ".join(self.word_so_far))

    def is_letter_guessed(self, letter):
        return letter in self.guessed_letters

    def is_letter_in_word(self, letter):
        return letter in self.word

    def show_message(self, message):
        tk.messagebox.showinfo("Hangman Game", message)
        self.window.destroy()

if __name__ == "__main__":
    game = HangmanGame()
    tk.mainloop()