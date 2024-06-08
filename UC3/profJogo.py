import random  # Importa a biblioteca random para escolher aleatoriamente as jogadas do computador
from getpass import getpass  # Importa a função getpass para ocultar a entrada do usuário

# Função para obter a escolha do usuário
def obter_escolha_usuario(jogador):
    escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]  # Lista de escolhas possíveis
    # Solicita ao jogador que escolha uma das opções
    escolha_usuario = getpass(f"{jogador}, escolha pedra, papel, tesoura, lagarto ou spock: ").lower()
    # Verifica se a escolha do usuário é válida
    while escolha_usuario not in escolhas:
        print("Escolha inválida. Tente novamente.")  # Mensagem de erro se a escolha for inválida
        # Solicita novamente até que uma escolha válida seja feita
        escolha_usuario = getpass(f"{jogador}, escolha pedra, papel, tesoura, lagarto ou spock: ").lower()
    return escolha_usuario  # Retorna a escolha válida do usuário

# Função para obter a escolha do computador
def obter_escolha_computador():
    escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]  # Lista de escolhas possíveis
    return random.choice(escolhas)  # Retorna uma escolha aleatória

# Função para determinar o vencedor com base nas escolhas
def determinar_vencedor(escolha1, escolha2):
    # Dicionário com as combinações vencedoras
    combinacoes_vencedoras = {
        "tesoura": ["papel", "lagarto"],
        "papel": ["pedra", "spock"],
        "pedra": ["lagarto", "tesoura"],
        "lagarto": ["spock", "papel"],
        "spock": ["tesoura", "pedra"]
    }
    # Verifica se as escolhas são iguais, resultando em empate
    if escolha1 == escolha2:
        return "Empate!"
    # Verifica se escolha2 está na lista de combinações vencedoras de escolha1
    elif escolha2 in combinacoes_vencedoras[escolha1]:
        return "Escolha 1 venceu!"  # Retorna que a escolha1 venceu
    else:
        return "Escolha 2 venceu!"  # Retorna que a escolha2 venceu

# Função para jogar no modo PvM (Player vs. Machine)
def jogar_pvm():
    escolha_usuario = obter_escolha_usuario("Usuário")  # Obtém a escolha do usuário
    escolha_computador = obter_escolha_computador()  # Obtém a escolha do computador
    print(f"Você escolheu: {escolha_usuario}")  # Exibe a escolha do usuário
    print(f"O computador escolheu: {escolha_computador}")  # Exibe a escolha do computador
    resultado = determinar_vencedor(escolha_usuario, escolha_computador)  # Determina o vencedor
    print(resultado)  # Exibe o resultado

# Função para jogar no modo PvP (Player vs. Player)
def jogar_pvp():
    escolha_jogador1 = obter_escolha_usuario("Jogador 1")  # Obtém a escolha do jogador 1
    escolha_jogador2 = obter_escolha_usuario("Jogador 2")  # Obtém a escolha do jogador 2

    resultado = determinar_vencedor(escolha_jogador1, escolha_jogador2)  # Determina o vencedor
    print(f"Jogador 1 escolheu: {escolha_jogador1}")  # Exibe a escolha do jogador 1
    print(f"Jogador 2 escolheu: {escolha_jogador2}")  # Exibe a escolha do jogador 2
    print(resultado)  # Exibe o resultado

# Solicita ao usuário que escolha o modo de jogo (PvM ou PvP)
modo = input("Escolha o modo de jogo (PvM ou PvP): ").lower()
# Verifica se o modo de jogo escolhido é válido
while modo not in ["pvm", "pvp"]:
    print("Modo inválido. Tente novamente.")  # Mensagem de erro se o modo for inválido
    modo = input("Escolha o modo de jogo (PvM ou PvP): ").lower()
# Inicia o jogo no modo escolhido
if modo == "pvm":
    jogar_pvm()
else:
    jogar_pvp()
