import tkinter as tk
import random

def Choose_Word(data):
    int_Rows_datei = 0
    for x in data:
        int_Rows_datei = int_Rows_datei + 1
    Random_int = (random.randint(0,int_Rows_datei))
    Random_int = Random_int  - 1
    Hangman_Word = data[Random_int]
    Hangman_Word = Hangman_Word.lower()
    return Hangman_Word

window = tk.Tk()
window.title("Hangman")
my_datei = open("Hangman_words.txt","r",encoding="UTF8")

Hangman_Images = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

