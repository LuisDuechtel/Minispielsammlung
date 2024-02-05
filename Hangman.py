import random
import tkinter as tk

hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]
my_datei = open("Hangman_words.txt","r",encoding="UTF8")
eingegebene_Buchstaben = []
correct_guess = 0
max_versuche = 12
int_versuche = 0
guess =""
data = my_datei.read().splitlines()
GUI = tk.Tk()
GUI.title("Hangman")

Hangman_Label = tk.Label(GUI, font=("CourierK", 16))
Hangman_Label.grid(row=0, column=0)



def save_guess():
    global guess
    guess = guess_entry.get()
    return guess

guess_entry=tk.Entry(GUI, width=3, font=("Arial", 25))
guess_entry.grid(row=2,column=0)

Guess_button=tk.Button(GUI, text="Guess", command=save_guess)
Guess_button.grid(row=2,column=1)

Guess = save_guess()
print(Guess)

Result_Label=tk.Label(GUI,font=("Arial", 25))
Result_Label.grid(row=3,column=0)

def Try_Letters_GUI(eingegebene_Buchstaben):
    Try_Letters=tk.Label(GUI,text=eingegebene_Buchstaben, font=("Arial", 25))
    Try_Letters.grid(row=4,column=0)

def Info_GUI(Info,eingegebene_Buchstaben):
    Info=tk.Label(GUI, text=Info, font=("Arial", 25))
    Info.grid(row=5,column=0)

def Choose_Word(data):
    int_Rows_datei = 0
    for x in data:
        int_Rows_datei = int_Rows_datei + 1
    Random_int = (random.randint(0,int_Rows_datei))
    Random_int = Random_int  - 1
    Hangman_Word = data[Random_int]
    Hangman_Word = Hangman_Word.lower()
    return Hangman_Word

def update_Hangman(mistake):
    Hangman_Label.config(text=hangman_art[mistake])

def create_underscore_String(Len_word):
    Underscore_String = []
    i = 0
    while i <= Len_word:
        Underscore_String.append("_")
        i = i + 1
    Word_with_blanks = (" ".join(Underscore_String))
    word_label = tk.Label(GUI, text=Word_with_blanks, font=("Arial",20))
    word_label.grid(row=1,column=0)
    return Word_with_blanks

"""
Hangman_Word = Choose_Word(data)
Len_word = (len(Hangman_Word))
Word_with_blanks = create_underscore_String(Len_word)

while (correct_guess < Len_word):
    if len(eingegebene_Buchstaben) != 0:
        Try_Letters_GUI(eingegebene_Buchstaben)   
    
    input_Letter = input_Letter.lower()
    if len(input_Letter) > 1:
        print("SO NICHT!. Ein Buchstabe eingeben!")
    elif input_Letter ==  "":
        print("Nichts eingeben geht auch nicht!")
    else:
        if input_Letter in eingegebene_Buchstaben:
            print("Hast du schonmal eingeben!")
        else:
            eingegebene_Buchstaben.append(input_Letter)
            if input_Letter in Hangman_Word:
                index_counter = 0
                print("Buchstabe ist vorhanden")
                for One_Letter in Hangman_Word:
                    if One_Letter == input_Letter:
                        correct_guess = correct_guess + 1
                        Underscore_String[index_counter] = input_Letter
                    index_counter = index_counter + 1    
                print(" ".join(Underscore_String))
            else:
                int_versuche = int_versuche + 1
                print("Leider nicht vorhanden")
                Versuche_Uebrig = max_versuche - int_versuche
                if Versuche_Uebrig == 0:
                    break
                else:
                    print(f"Du hast noch {Versuche_Uebrig} Versuche übrig!")


if int_versuche >= max_versuche:
    print("Leider nicht geschafft - Maximale Anzahl an Versuche erreicht")
else:
    print("Wort korrekt!")
print("Das gesuchte Wort war: " + Hangman_Word)
"""
GUI.mainloop()
print(guess)