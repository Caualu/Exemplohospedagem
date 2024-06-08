import random

cadeia = {
    "pedra": ["tesoura", "lagarto"],
    "papel": ["pedra", "spock"],
    "tesoura": ["papel", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tesoura", "pedra"]
}

def funcaomaquina():
    possibilidades = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    return random.choice(possibilidades)

def funcaovencedor(a, b):
        if a == b:
            return "empate"
        # a = pedra // b = tesoura
        elif b in cadeia[a]:
            return "Jogador 1 vencedor"
        else:
            return "Jogador 2 vencedor"
    

def funcaoescolha():
    possibilidades = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    while True:
        possib = input("Escolha entre PEDRA, PAPEL, TESOURA, LAGARTO ou SPOCK: \n").lower()
        if possib in possibilidades:
            return possib
        print("Por favor, escolha entre PEDRA, PAPEL, TESOURA, LAGARTO ou SPOCK. \n")



print("Bem vindo ao pedra, papel, tesoura, lagarto e spock.")

while True:
    contra = int(input("Escolha 1 para jogar com alguém \n Escolha 2 para jogar com o computador.\n"))

    if contra == 2:
        jogador = funcaoescolha()
        cpu = funcaomaquina()

        print(f"Jogador: {jogador}")
        print(f"Computador: {cpu}")

        resultado = funcaovencedor(jogador, cpu)
        print(f"Resultado: {resultado}")

    elif contra == 1:
        jogador1 = funcaoescolha()
        jogador2 = funcaoescolha()

        print(f"Jogador 1: {jogador1}")
        print(f"Jobador 2: {jogador2}")

        resultado = funcaovencedor(jogador1, jogador2)
        print(f"Resultado: {resultado}")

    else:
        print("Por favor, digite 1 para jogar com alguém e 2 para jogar com o computador.")

    continuar = int(input("Deseja seguir jogando? \n 1 para SIM. \n 2 para NÃO."))
    if continuar == 2:
        break