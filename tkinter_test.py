import tkinter as tk
import tkinter.ttk as ttk
from random import randint

window = tk.Tk()
window.title("Jokenpo")
window.minsize(500, 400)
window.configure(bg="#ffffff")

playerSelection = tk.StringVar()
computerSelection = tk.StringVar()
result = tk.StringVar()

gameOptions = ["pedra", "papel", "tesoura"]
resultOptions = ["Vitória", "Derrota", "Empate"]

title = tk.Label(window, text="Jogo: Pedra, Papel e Tesoura", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

label_computer = tk.Label(window, textvariable=computerSelection, font=("Arial", 14), bg="#f0f0f0")
label_computer.pack(pady=5)

label_result = tk.Label(window, textvariable=result, font=("Arial", 20, "bold"), bg="white", width=20)
label_result.pack(pady=20)

frm = ttk.Frame(window, padding=30)
frm.pack()

frame_buttons = tk.Frame(window, bg="#f0f0f0")
frame_buttons.pack(pady=10)

def Play(choice):
    playerSelection.set(choice)
    computer = gameOptions[randint(0, 2)]
    computerSelection.set = (f"Computador escolheu: {computer}")
    player = choice

    if computer == player:
        result.set(resultOptions[2])
    elif (player == gameOptions[0] and computer == gameOptions[2]) or \
        (player == gameOptions[1] and computer == gameOptions[0]) or \
        (player == gameOptions[2] and computer == gameOptions[1]):
        result.set(resultOptions[0])
    else:
        result.set(resultOptions[1])

for nome in gameOptions:
    btn = tk.Button(
        frame_buttons, text=nome.capitalize(), width=10, height=2,
        bg="#666", fg="white", font=("Arial", 12),
        command=lambda n=nome: Play(n)
    )
    btn.pack(side="left", padx=10)

window.mainloop()