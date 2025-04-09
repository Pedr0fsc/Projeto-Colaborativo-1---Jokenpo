import tkinter as tk
import tkinter.ttk as ttk
from random import randint

window = tk.Tk()
window.title("Jokenpo")
window.minsize(500, 400)

frm = ttk.Frame(window, padding=30)
frm.grid()

playerSelection = tk.StringVar()
result = tk.StringVar()

gameOptions = ["pedra", "papel", "tesoura"]
resultOptions = ["Vitória", "Derrota", "Empate"]

def Play(choice):
    playerSelection.set(choice)
    computerChoice = randint(0, 2)
    computer = gameOptions[computerChoice]
    player = choice

    if computer == player:
        result.set(resultOptions[2])
    elif (player == gameOptions[0] and computer == gameOptions[2]) or \
        (player == gameOptions[1] and computer == gameOptions[0]) or \
        (player == gameOptions[2] and computer == gameOptions[1]):
        result.set(resultOptions[0])
    else:
        result.set(resultOptions[1])

lbl = tk.Label(window, textvariable=result, fg="black", bg="white", font=("Arial", 20))
lbl.grid(row=3, column=2)

btn_opcoes = tk.Button(text="Pedra", fg="white", bg="gray", width=10, height=5, padx=5, pady=5, command=lambda: Play(gameOptions[0])).grid(row=1, column=1)
btn_opcoes = tk.Button(text="Papel", fg="white", bg="gray", width=10, height=5, padx=5, pady=5, command=lambda: Play(gameOptions[1])).grid(row=1, column=2)
btn_opcoes = tk.Button(text="Tesoura", fg="white", bg="gray", width=10, height=5, padx=5, pady=5, command=lambda: Play(gameOptions[2])).grid(row=1, column=3)

window.mainloop()