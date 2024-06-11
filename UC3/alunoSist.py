nome_arquivo = 'cadastro.txt'
num_cadastro = int(input("Digite o número de cadastros a serem adicionados: "))

for i in range(num_cadastro):
    # Coletando informações do cadastro 
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = input("Digite sua idade: ")
    cpf = input("Digite seu cpf: ")
    email = input("Digite seu email: ")

    # Armazenando as informações em um dicionário
    cadastro  = {
        'Nome': nome,
        'sobrenome': sobrenome,
        'Idade': idade,
        'cpf': cpf,
        'email': email
    }

    # Abrindo o arquivo e escrevendo o conteúdo do currículo
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write("Cadastro:\n")
        for chave, valor in cadastro.items():
            arquivo.write(f"{chave}: {valor}\n")
        arquivo.write("\n")

    print(f"cadastro  de {nome} adicionado com sucesso.")

print("Todos os cadastros  foram adicionados ao arquivo.")
