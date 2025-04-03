import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.minsize(500, 400)

frm = ttk.Frame(window, padding=30)
frm.grid()

playerSelection = tk.StringVar()

lbl = tk.Label(window, textvariable=playerSelection, fg="black", bg="#b3b3ff")
lbl.grid(row=3, column=2)
btn_opcoes = tk.Button(text="Pedra", fg="white", bg="gray", width=10, height=5, padx=5, pady=5, command=lambda: playerSelection.set("pedra")).grid(row=1, column=1)
btn_opcoes = tk.Button(text="Papel", fg="white", bg="gray", width=10, height=5, padx=5, pady=5, command=lambda: playerSelection.set("papel")).grid(row=1, column=2)
btn_opcoes = tk.Button(text="Tesoura", fg="white", bg="gray", width=10, height=5, padx=5, pady=5, command=lambda: playerSelection.set("tesoura")).grid(row=1, column=3)

window.mainloop()