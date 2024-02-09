import tkinter as tk
import random

def spiel():
    def get_user_choice(choice):
        user_choice_label.config(text=f"Deine Wahl: {choice}")
        computer_choice = random.choice(choices)
        computer_choice_label.config(text=f"Computer wählt: {computer_choice}")

        if choice == computer_choice:
            result_label.config(text="Unentschieden!")
        elif (choice == "Schere" and computer_choice == "Papier") or \
             (choice == "Stein" and computer_choice == "Schere") or \
             (choice == "Papier" and computer_choice == "Stein"):
            result_label.config(text="Du gewinnst!")
        else:
            result_label.config(text="Der Computer gewinnt!")

    choices = ["Schere", "Stein", "Papier"]

    root = tk.Tk()
    root.title("Schere-Stein-Papier-Spiel")
    root.geometry("400x200")  # Hier wird die Größe des Fensters festgelegt

    user_choice_label = tk.Label(root, text="Deine Wahl:")
    user_choice_label.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    for choice in choices:
        button = tk.Button(button_frame, text=choice, command=lambda c=choice: get_user_choice(c))
        button.pack(side=tk.LEFT)

    computer_choice_label = tk.Label(root, text="Computer wählt:")
    computer_choice_label.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    spiel()
