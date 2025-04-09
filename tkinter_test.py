import tkinter as tk
import tkinter.ttk as ttk
from random import randint

# Configurações básicas do aplicativo

window = tk.Tk()
window.title("Jokenpo")
window.minsize(500, 400)
window.configure(bg="#ffffff")

# Frames de menu e fases

frame_menu = tk.Frame(window, bg="#ffffff")
frame_pvc = tk.Frame(window, bg="#ffffff")
frame_pvp = tk.Frame(window, bg="#ffffff")

def show_frame(f):
    f.tkraise()

for frame in (frame_menu, frame_pvc, frame_pvp):
    frame.grid(row=0, column=0, sticky="nsew")

show_frame(frame_menu)

game_title = tk.Label(frame_menu, text="Jokenpô!", font=("Arial", 18, "bold"), bg="#ffffff")
game_title.pack(pady=10)
btn_pvc = tk.Button(frame_menu, text="Player vs Computador", font=("Arial", 15, "bold"), command=lambda: show_frame(frame_pvc))
btn_pvc.pack(pady=10)
btn_pvp = tk.Button(frame_menu, text="Player vs Player", font=("Arial", 15, "bold"), command=lambda: show_frame(frame_pvp))
btn_pvp.pack(pady=10)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# ---------------------------------------------------------------------------------------------------------------------------------------
# FRAME - PVC
# Variáveis

playerSelection = tk.StringVar()
computerSelection = tk.StringVar()
result = tk.StringVar()

gameOptions = ["pedra", "papel", "tesoura"]
resultOptions = ["Vitória", "Derrota", "Empate"]

score = {
    "Vitória" : 0,
    "Derrota" : 0,
    "Empate"  : 0
}

# Labels - Elementos visuais

# Top Bar
top_bar_pvc = tk.Frame(frame_pvc, bg="#ffffff")
top_bar_pvc.pack(fill="x", padx=10, pady=10)

arrow_back_img = tk.PhotoImage(file="arrow_back.png")
btn_return = tk.Button(top_bar_pvc, image=arrow_back_img, compound="left", command=lambda : show_frame(frame_menu))
btn_return.image = arrow_back_img
btn_return.grid(row=0, column=0, sticky="w")

pvc_title = tk.Label(top_bar_pvc, text="Jogo: Pedra, Papel e Tesoura / PVC", font=("Arial", 18, "bold"), bg="#ffffff")
pvc_title.grid(row=0, column=1)

top_bar_pvc.grid_columnconfigure(0, weight=1)
top_bar_pvc.grid_columnconfigure(1, weight=1)
top_bar_pvc.grid_columnconfigure(2, weight=1)


label_computer = tk.Label(frame_pvc, textvariable=computerSelection, font=("Arial", 14), bg="#ffffff")
label_computer.pack(pady=5)

label_result = tk.Label(frame_pvc, textvariable=result, font=("Arial", 15, "bold"), bg="#ffffff", width=26)
label_result.pack(pady=20)

frm = ttk.Frame(frame_pvc, padding=30)
frm.pack()

frame_buttons = tk.Frame(frame_pvc, bg="#ffffff")
frame_buttons.pack(pady=10)

buttons = []

# Funções de jogo

def play(playerSelection):
    computerSelection.set("")
    result.set("Computador está pensando...")
    label_result.config(bg="white", fg="black")

    for b in buttons:
        b.config(state="disabled")

    frame_pvc.after(1500, lambda: jo_ken_po_sequence(playerSelection))

def jo_ken_po_sequence(playerSelection):
    result.set("Jo...")
    frame_pvc.after(500, lambda: result.set("Ken..."))
    frame_pvc.after(1000, lambda: result.set("Pô!..."))
    frame_pvc.after(1500, lambda: play_process(playerSelection))

def play_process(playerSelection):
    computador = gameOptions[randint(0, 2)]
    computerSelection.set(f"Computador escolheu: {computador.capitalize()}")
    
    if playerSelection == computador:
        result.set("Empate")
        score["Empate"] += 1
        label_result.config(bg="#3399ff", fg="white")
    elif (playerSelection == "pedra" and computador == "tesoura") or \
         (playerSelection == "papel" and computador == "pedra") or \
         (playerSelection == "tesoura" and computador == "papel"):
        result.set("Vitória")
        score["Vitória"] += 1
        label_result.config(bg="#33cc33", fg="white")
    else:
        result.set("Derrota")
        score["Derrota"] += 1
        label_result.config(bg="#ff3333", fg="white")

    label_score.config(text=f"Vitórias: {score['Vitória']} | Derrotas: {score['Derrota']} | Empates: {score['Empate']}")

    for b in buttons:
        b.config(state="normal")

# Label dos botões e pontuação

for nome in gameOptions:
    btn = tk.Button(
        frame_buttons, text=nome.capitalize(), width=10, height=2,
        bg="#666", fg="white", font=("Arial", 12),
        command=lambda n=nome: play(n)
    )
    btn.pack(side="left", padx=10)
    buttons.append(btn)

label_score = tk.Label(frame_pvc, text="Vitória: 0 | Derrotas: 0 | Empates: 0", font=("Arial", 15, "bold"), bg="#ffffff", width=30)
label_score.pack(pady=50)

# --------------------------------------------------------------------------------------------------------------------------------------
# FRAME - PVP

# Top Bar
top_bar_pvp = tk.Frame(frame_pvp, bg="#ffffff")
top_bar_pvp.pack(fill="x", padx=10, pady=10)

arrow_back_img = tk.PhotoImage(file="arrow_back.png")
btn_return = tk.Button(top_bar_pvp, image=arrow_back_img, compound="left", command=lambda : show_frame(frame_menu))
btn_return.image = arrow_back_img
btn_return.grid(row=0, column=0, sticky="w")

pvc_title = tk.Label(top_bar_pvp, text="Jogo: Pedra, Papel e Tesoura / PVP", font=("Arial", 18, "bold"), bg="#ffffff")
pvc_title.grid(row=0, column=1)

top_bar_pvp.grid_columnconfigure(0, weight=1)
top_bar_pvp.grid_columnconfigure(1, weight=1)
top_bar_pvp.grid_columnconfigure(2, weight=1)


# --------------------------------------------------------------------------------------------------------------------------------------
window.mainloop()