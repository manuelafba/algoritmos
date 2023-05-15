numeros = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros = [numero] + numeros

for i in range(10):
    print(numeros[i])