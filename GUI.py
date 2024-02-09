import tkinter as tk
from subprocess import call

def button1_clicked():
    call(["python", "Hangman_V2.py"])

def button2_clicked():
    call(["python", "tictactoe.py"])

def button3_clicked():
    call(["python", "SchereSteinPapier.py"])


root = tk.Tk()
root.geometry("300x150")
root.title("Spielesammlung DHBW Bad Mergentheim")

button1 = tk.Button(root, text="Hangman", command=button1_clicked)
button1.pack(pady=10)

button2 = tk.Button(root, text="tictactoe", command=button2_clicked)
button2.pack(pady=10)

button3 = tk.Button(root, text="Schere Stein Paar Bier", command=button3_clicked)
button3.pack(pady=10)

root.mainloop()
