# desenvolva um programa que solicite nome de livro e guarde em arquivo.txt
#Especificar o nome do arquivo e o conteudo 
nome_arquivo = 'exemplo.txt'
livro = int(input("digite o numero de livros que voce deseja salvar:"))


for i in range(livro):
    autor = input("dga o nome do autor:")
    conteudo = input("diga o nome dos seu livro que deseja guardar:")
    #Abrir o arquivo no modo de escrita e escrever o conteudo
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.writelines(f"{autor}\n{conteudo}\n")

    print(f" livro adicionado com sucesso.")
