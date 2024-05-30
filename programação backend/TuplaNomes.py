# Pedindo ao usuário para inserir três valores
entrada = input("Digite cinco nomes separados por vírgulas: ")
valores = entrada.split(",")  # Isso cria uma lista dos valores
minha_tupla = tuple(valores)  # Convertendo a lista em uma tupla

# Mostrando cada elemento da tupla
print("Os nomes inseridos foram:")
for elemento in minha_tupla:
    print(elemento)

 