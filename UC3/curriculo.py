nome_arquivo = 'curriculos.txt'
num_curriculos = int(input("Digite o número de currículos a serem adicionados: "))

for i in range(num_curriculos):
    # Coletando informações do currículo
    nome = input("Digite seu nome completo: ")
    idade = input("Digite sua idade: ")
    experiencia = input("Digite sua experiência profissional: ")
    habilidades = input("Digite suas habilidades: ")

    # Armazenando as informações em um dicionário
    curriculo = {
        'Nome': nome,
        'Idade': idade,
        'Experiência': experiencia,
        'Habilidades': habilidades
    }

    # Abrindo o arquivo e escrevendo o conteúdo do currículo
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write("Currículo:\n")
        for chave, valor in curriculo.items():
            arquivo.write(f"{chave}: {valor}\n")
        arquivo.write("\n")

    print(f"Curriculo de {nome} adicionado com sucesso.")

print("Todos os currículos foram adicionados ao arquivo.")
