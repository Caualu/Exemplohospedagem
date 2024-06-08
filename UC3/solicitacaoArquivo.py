salvando = int(input("Digite o  que deseja salvar: "))

for i in range(1):
    # Coletando informações do 
    nome = input("Digite seu nome completo: ")
    idade = input("Digite sua idade: ")
    experiencia = input("Digite sua experiência profissional: ")
    habilidades = input("Digite suas habilidades: ")
    titulo = input("Digite o título do livro que deseja guardar: ")
    # Armazenando as informações em um dicionário
    curriculo = {
        'Nome': nome,
        'Idade': idade,
        'Experiência': experiencia,
        'Habilidades': habilidades
    }
    
    # Modificando o nome do arquivo com base no nome do 
    nome_arquivo = f"{titulo}.txt"
# Abrindo o arquivo e escrevendo o conteúdo do currículo
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write("Currículo:\n")
        for chave, valor in curriculo.items():
            arquivo.write(f"{chave}: {valor}\n")
        arquivo.write("\n")

    print(f"Curriculo de {nome} adicionado com sucesso.")

print("Todos os currículos foram adicionados ao arquivo.")







