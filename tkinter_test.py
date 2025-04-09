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

title = tk.Label(window, text="Jogo: Pedra, Papel e Tesoura", font=("Arial", 18, "bold"), bg="#ffffff")
title.pack(pady=10)

label_computer = tk.Label(window, textvariable=computerSelection, font=("Arial", 14), bg="#ffffff")
label_computer.pack(pady=5)

label_result = tk.Label(window, textvariable=result, font=("Arial", 15, "bold"), bg="#ffffff", width=26)
label_result.pack(pady=20)

frm = ttk.Frame(window, padding=30)
frm.pack()

frame_buttons = tk.Frame(window, bg="#f0f0f0")
frame_buttons.pack(pady=10)

def play(playerSelection):
    result.set("O computador está escolhendo...")
    label_result.config(bg="white", fg="black")

    window.after(1000, lambda: play_process(playerSelection))

def play_process(playerSelection):
    computer = gameOptions[randint(0, 2)]
    computerSelection.set = (f"Computador escolheu: {computer}")

    if computer == playerSelection:
        result.set(resultOptions[2])
        label_result.config(bg="yellow", fg="white")
    elif (playerSelection == gameOptions[0] and computer == gameOptions[2]) or \
        (playerSelection == gameOptions[1] and computer == gameOptions[0]) or \
        (playerSelection == gameOptions[2] and computer == gameOptions[1]):
        result.set(resultOptions[0])
        label_result.config(bg="green", fg="white")
    else:
        result.set(resultOptions[1])
        label_result.config(bg="red", fg="white")

for nome in gameOptions:
    btn = tk.Button(
        frame_buttons, text=nome.capitalize(), width=10, height=2,
        bg="#666", fg="white", font=("Arial", 12),
        command=lambda n=nome: play(n)
    )
    btn.pack(side="left", padx=10)

window.mainloop()