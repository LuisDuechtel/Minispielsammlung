import tkinter as tk
from functools import partial
import random

class MinispielSammlung:
    def __init__(self, root):
        self.root = root
        self.root.title("Minispiel-Sammlung")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.create_buttons()

    def create_buttons(self):
        spiele = ["Schere-Stein-Papier", "AnderesSpiel"]  # Füge hier weitere Spiele hinzu

        for spiel in spiele:
            button = tk.Button(self.frame, text=spiel, command=partial(self.starte_spiel, spiel))
            button.pack(pady=10)

    def starte_spiel(self, spiel):
        if spiel == "Schere-Stein-Papier":
            self.starte_schere_stein_papier()
        # Füge hier weitere Spiele hinzu

    def starte_schere_stein_papier(self):
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

        self.root.withdraw()  # Verstecke das Hauptfenster während des Spiels

        root_ssp = tk.Toplevel()
        root_ssp.title("Schere-Stein-Papier-Spiel")
        root_ssp.geometry("400x200")

        user_choice_label = tk.Label(root_ssp, text="Deine Wahl:")
        user_choice_label.pack()

        button_frame = tk.Frame(root_ssp)
        button_frame.pack()

        for choice in choices:
            button = tk.Button(button_frame, text=choice, command=lambda c=choice: get_user_choice(c))
            button.pack(side=tk.LEFT)

        computer_choice_label = tk.Label(root_ssp, text="Computer wählt:")
        computer_choice_label.pack()

        result_label = tk.Label(root_ssp, text="")
        result_label.pack()

        root_ssp.protocol("WM_DELETE_WINDOW", self.zurueck_zum_hauptfenster)

    def zurueck_zum_hauptfenster(self):
        self.root.deiconify()  # Stelle das Hauptfenster wieder her
        root_ssp.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MinispielSammlung(root)
    root.mainloop()
