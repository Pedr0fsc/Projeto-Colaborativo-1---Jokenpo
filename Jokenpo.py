from random import randint
from time import sleep

opcoes = ["pedra", "papel", "tesoura"]

computador = randint(0, 2)

print("Bem vindo ao Jokenpo!")
sleep(1)
print("Essas são as suas opções: \n[0] - Pedra\n[1] - Papel\n[2] - Tesoura")

jogador = int(input("Digite a sua escolha: "))

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)

print("Você jogou", jogador, "e o computador jogou", computador)

match computador:
    case 0:
        if jogador == 0:
            print("Empate!")
        elif jogador == 1:
            print("Vitória!")
        else:
            print("Derrota!")
    case 1:
        if jogador == 0:
            print("Derrota!")
        elif jogador == 1:
            print("Empate!")
        else:
            print("Vitória!")
    case 2:
        if jogador == 0:
            print("Vitória!")
        elif jogador == 1:
            print("Derrota!")
        else:
            print("Empate!2")