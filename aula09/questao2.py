cont = 0
soma = 0
while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    if numero > 0:
        cont += 1
        soma = numero + soma
    else:
        break
print(f"A média dos números positivos digitados é {soma/cont}")