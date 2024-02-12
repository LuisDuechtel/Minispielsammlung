from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
import pygame
pygame.init()

custom_sound_path = "golfclap.mp3"
pygame.mixer.music.load(custom_sound_path)


my_datei = open("Hangman_words.txt", "r", encoding="UTF8")
data = my_datei.read().splitlines()
Label_created = False
GUI = Tk()
GUI.title("Hangman")
GUI.geometry("600x400")
photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
          PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def Choose_Word(data):
    global Hangman_Word
    int_Rows_datei = len(data)
    Random_int = random.randint(0, int_Rows_datei - 1)
    Hangman_Word = data[Random_int]
    Hangman_Word = Hangman_Word.upper()
    return Hangman_Word

def create_underscore_String(Len_word):
    global Underscore_String
    global word_label
    global Label_created
    Underscore_String = ["_"] * Len_word
    Word_with_blanks = " ".join(Underscore_String)
    if Label_created == True:
        word_label.destroy()
    word_label = Label(GUI, text=Word_with_blanks, font=("Arial", 20))
    Label_created = True
    word_label.grid(row=3, column=0, columnspan=9)
    return Word_with_blanks

def newGame(data):
    global Hangman_Word
    global Len_word
    global Word_with_blanks
    global int_versuche
    global correct_guess
    correct_guess = 0
    int_versuche = 0
    Hangman_Word = Choose_Word(data)
    Len_word = len(Hangman_Word)
    print(Hangman_Word)
    Word_with_blanks = create_underscore_String(Len_word)


def make_guess(Letter):
    global correct_guess, int_versuche, Underscore_String, Word_with_blanks
    Word_without_blanks = ""
    if int_versuche < 11:
        if Letter in Hangman_Word:
            index_counter = 0
            for One_Letter in Hangman_Word:
                if One_Letter == Letter:
                    correct_guess += 1
                    Underscore_String[index_counter] = Letter
                index_counter += 1
            Word_with_blanks = " ".join(Underscore_String)
            word_label.config(text=Word_with_blanks)
            Word_without_blanks = Word_with_blanks.replace(" ", "")
            
        else:
            int_versuche += 1
            imgLabel.config(image=photos[int_versuche])
        
        if Word_without_blanks == Hangman_Word:
            pygame.mixer.music.play()
            messagebox.showinfo("Gewonnen!", f"Herzlichen Glückwunsch! Du hast das Wort '{Hangman_Word}' richtig erraten.")
    
    else:
        messagebox.showinfo("Verloren!", f"Du hast das Wort: '{Hangman_Word}' NICHT erraten.")

imgLabel = Label(GUI)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

n = 0
for c in ascii_uppercase:
    Button(GUI, text=c, command=lambda c=c: make_guess(c), font=('Helvetica 18'), width=4).grid(row=5 + n // 9, column=n % 9)
    n += 1

new_game_button = Button(GUI, text="Neues\nSpiel", command=lambda: newGame(data), font=("Helvetica 10 bold"))
new_game_button.grid(row=5 + n // 9, column=n % 9) 

newGame(data)
GUI.mainloop()
