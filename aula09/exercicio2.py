cont = 0
soma = 0
while True:
    numero = int(input("Digite um número positivo: "))
    if numero == 0:
        break
    if numero > 0:
        cont += 1
        soma = numero + soma
    else:
        print("Você digitou um número negativo")

media = soma/cont

print(f"A média dos núemros digitados é {media}")