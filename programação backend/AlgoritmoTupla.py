# Pedindo ao usuário para inserir três valores
entrada = input("Digite cinco nomes separados por vírgulas: ")
nomes = entrada.split(",")  # Isso cria uma lista dos valores
minha_tupla = tuple(nomes)  # Convertendo a lista em uma tupla
if len(nomes) != 5:
    print("voce nao isneriu cinco nomes exatamente.")

else:
    nome_inserido = input("digite um nome para verificar se esta na tupla:")

    if nome_inserido in nomes:
        print("o nome esta na lista")

    else:
        ("o nome nao esta na tupla")    

