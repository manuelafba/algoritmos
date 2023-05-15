somapos = 0
negativos = 0

for i in range (20):
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        somapos += numero
    elif numero < 0:
        negativos += 1

print(f"A soma dos números positivos é {somapos} e a quantidade de números negativos é {negativos}")