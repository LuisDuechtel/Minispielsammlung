import tkinter as tk
root = tk.Tk()

def button1_clicked():
    print("Button 1 was clicked!")

def button2_clicked():
    print("Button 2 was clicked!")

def button3_clicked():
    print("Button 3 was clicked!")

root.title("Test")

Label_Text = "Hallo! Wilkommen!"
Label = tk.Label(root, text=Label_Text, font=("Arial", 15, "bold"))
Label.grid(row=0, column=0)

Label_Name_text = "Bitte Namen eingeben"
Label_Name = tk.Label(root, text=Label_Name_text, font=("Arial", 10, "bold"))
Label_Name.grid(row=1, column=0)

eingabefeld_wert=tk.StringVar()
eingabefeld=tk.Entry(root, textvariable=eingabefeld_wert)
eingabefeld.grid(row=1, column=1)

button1 = tk.Button(root, text="Button 1", command=button1_clicked)
button1.grid(row=3, column=0, sticky="e")

button2 = tk.Button(root, text="Button 2", command=button2_clicked)
button2.grid(row=3, column=1, sticky="e")

button3 = tk.Button(root, text="Button 3", command=button3_clicked)
button3.grid(row=3, column=2, sticky="e")
root.mainloop()