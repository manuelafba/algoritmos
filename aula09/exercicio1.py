cont = 0
while True:
    numero = int(input("Digite um número positivo: "))
    if numero == 0:
        break
    if numero > 0:
        cont += 1
    else:
        print("Você digitou um número negativo")

print(f"A quantidade de números digitados foi {cont}")