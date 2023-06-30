numero = int(input("Digite um número inteiro:"))

if numero > 0 and numero % 2 == 0:
    print("Número positivo e par")
elif numero > 0 and numero % 2 == 1:
    print("Número positivo e ímpar")
elif numero < 0 and numero % 2 == 0:
    print("Número negativo e par")
elif numero < 0 and numero % 2 == 1:
    print("Número negativo e ímpar")
