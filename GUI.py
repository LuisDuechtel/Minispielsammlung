import tkinter as tk
from subprocess import call

def button1_clicked():
    call(["python", "Hangman_V2.py"])

def button2_clicked():
    call(["python", "tictactoe.py"])

def button3_clicked():
    call(["python", "SchereSteinPapier.py"])

root = tk.Tk()
root.geometry("1200x800")
root.title("Spielesammlung DHBW Bad Mergentheim")


background_image = tk.PhotoImage(file="assets/clouds.png")  
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

label = tk.Label(root, bg="#e4eaff", text="Minispielsammlung von Robin, Luis und Philipp", font=("Arial, 20"))
label.pack(pady=20)

button1 = tk.Button(root, text="Hangman", command=button1_clicked)
button1.pack(pady=10)

button2 = tk.Button(root, text="tictactoe", command=button2_clicked)
button2.pack(pady=10)

button3 = tk.Button(root, text="Schere Stein Papier", command=button3_clicked)
button3.pack(pady=10)

root.mainloop()
