qtdvalores = 0

while True:
    valor = int(input("Insira um número: (Digite 0 para encerrar) "))

    if valor == 0:
        break

    if 100 <= valor <= 200:
        qtdvalores += 1
        print(f"A quantidade de valores entre 100 e 200 digitados foi {qtdvalores}")