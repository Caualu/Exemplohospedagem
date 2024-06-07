def func(palavra):
    palavra1 = input("Insira uma palavra dentre essas opções (ping / time / vivo): ")

    if palavra1 == "ping":
        return "pong"
    elif palavra1 == "time":
        return "Botafogo"
    elif palavra1 == "vivo":
        return "morto"
    else:
        return "Palavra desconhecida."

print(func('palavra'))