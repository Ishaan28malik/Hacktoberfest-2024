import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

OPTIONS = ["Rock", "Paper", "Scissors"]

def on_click(option):
    computer_choice = random.choice(OPTIONS)
    result = decide_winner(option, computer_choice)
    messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result}")

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

for option in OPTIONS:
    button = tk.Button(button_frame, text=option, font=("Helvetica", 12, "bold"), width=10, pady=10, command=lambda o=option: on_click(o))
    button.pack(side=tk.LEFT, padx=10)

root.mainloop()
