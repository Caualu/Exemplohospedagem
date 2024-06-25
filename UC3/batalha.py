import numpy as np
import pygame

pygame.init()

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

music_file = 'C:\\Users\\62129532024.1\\Downloads\\Música triste do Naruto (1).mp3'
play_music(music_file)

# Mantenha o programa rodando para ouvir a música
input("Pressione Enter para parar a música...")

pygame.mixer.music.stop()
pygame.quit()








def jogo_batalha_naval():
    tamanho_tabuleiro = 5
    limite_tentativas = 7
    
    tabuleiro = np.zeros((tamanho_tabuleiro, tamanho_tabuleiro), dtype=int)
    posicao_navio = (np.random.randint(0, tamanho_tabuleiro), np.random.randint(0, tamanho_tabuleiro))



    tentativas = 0
    acertou = False
    
    print("\n=== Jogo Batalha Naval ===\n")
    print("Você tem que adivinhar onde está o navio!\n")
    
    while tentativas < limite_tentativas and not acertou:
        print("\nTabuleiro:")
        print(tabuleiro)
        
        linha = int(input("Adivinhe a linha (0-{}): ".format(tamanho_tabuleiro - 1)))
        coluna = int(input("Adivinhe a coluna (0-{}): ".format(tamanho_tabuleiro - 1)))
        
        if linha < 0 or linha >= tamanho_tabuleiro or coluna < 0 or coluna >= tamanho_tabuleiro:
            print("Posição inválida! Tente novamente.")
            continue
        
        tentativas += 1
        
        if (linha, coluna) == posicao_navio:
            print(f"Parabéns! Você acertou o navio em {tentativas} tentativas!")
            acertou = True
        else:
            if tabuleiro[linha, coluna] == -1:
                print("Você já tentou essa posição! Tente outra.")
            else:
                tabuleiro[linha, coluna] = -1
                # Feedback de proximidade
                if abs(linha - posicao_navio[0]) <= 1 and abs(coluna - posicao_navio[1]) <= 1:
                    print("Muito perto do navio!")
                else:
                    print("Errou! Tente novamente.")
    
    if not acertou:
        print(f"\nVocê não conseguiu encontrar o navio em {limite_tentativas} tentativas.")
        print(f"O navio estava na posição {posicao_navio}")




def gerar_posicoes_navios(num_navios, tamanho_tabuleiro):
    posicoes = []
    for _ in range(num_navios):
        posicao = (np.random.randint(0, tamanho_tabuleiro), np.random.randint(0, tamanho_tabuleiro))
        while posicao in posicoes:  # Garantir que não haja sobreposição de navios
            posicao = (np.random.randint(0, tamanho_tabuleiro), np.random.randint(0, tamanho_tabuleiro))
        posicoes.append(posicao)
    return posicoes

jogo_batalha_naval()