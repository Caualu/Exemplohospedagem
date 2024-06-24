import random

matriz = [[random.randint(0, 20) for _ in range(3)] for _ in range(3)]

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

valores_maiores_que_10 = [valor for linha in matriz for valor in linha if valor > 10]

print("\nValores maiores que 10:")
print(valores_maiores_que_10)
