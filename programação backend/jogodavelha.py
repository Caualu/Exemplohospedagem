# Primeiro, vamos criar uma função para imprimir o tabuleiro do jogo
def print_tabuleiro(tab):
    for i in range(3):
        for j in range(3):
            print(tab[i][j], end = ' ')
        print()

# Agora, vamos criar uma função para verificar se alguém ganhou o jogo
def check_vitoria(tab):
    # Verificando linhas
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] != ' ':
            return True
    # Verificando colunas
    for i in range(3):
        if tab[0][i] == tab[1][i] == tab[2][i] != ' ':
            return True
    # Verificando diagonais
    if tab[0][0] == tab[1][1] == tab[2][2] != ' ' or tab[0][2] == tab[1][1] == tab[2][0] != ' ':
        return True
    return False

# Finalmente, vamos criar o loop principal do jogo
def jogo():
    tab = [[' ']*3 for _ in range(3)]
    jogador = 'X'

    while True:
        print_tabuleiro(tab)
        linha = int(input("Digite a linha para o jogador " + jogador + ": "))
        coluna = int(input("Digite a coluna para o jogador " + jogador + ": "))
        if tab[linha][coluna] != ' ':
            print("Posição inválida! Tente novamente.")
            continue
        tab[linha][coluna] = jogador
        if check_vitoria(tab):
            print("O jogador " + jogador + " venceu!")
            break
        jogador = 'O' if jogador == 'X' else 'X'  # Trocando o jogador

jogo()
