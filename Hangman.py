import random

my_datei = open("Hangman_words.txt","r",encoding="UTF8")
int_Rows_datei = 0
Underscore_String = []
eingegebene_Buchstaben = []
correct_guess = 0
max_versuche = 12
int_versuche = 0

data = my_datei.read().splitlines()

for x in data:
    int_Rows_datei = int_Rows_datei + 1

Random_int = (random.randint(0,int_Rows_datei))
Random_int = Random_int  - 1
Hangman_Word = data[Random_int]
print("Willkommen zu HANGMAN")
Len_word = (len(Hangman_Word))
Hangman_Word = Hangman_Word.lower()
print("Das gesuchte Wort ist " + str(Len_word) + " Buchstaben lang")

i = 1
while i <= Len_word:
    Underscore_String.append("_")
    i = i + 1

print(" ".join(Underscore_String))

while (correct_guess < Len_word):
    print(Hangman_Word)
    if len(eingegebene_Buchstaben) != 0:
        print(f"Folgende Buchstaben wurden bereits eingegeben: {eingegebene_Buchstaben}")
    input_Letter = input("Welcher Buchstabe? Groß und Kleinschreibung egal!:  ")
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
print("Wort korrekt!")
print("Das gesuchte Wort war: " + Hangman_Word)


