from random import randint

vet = [0]*10
acima = [0]*10
soma = 0

for i in range(10):
    vet[i] = randint(0,10)
    soma += vet[i]
    media = soma/10

for i in range(10):
    if vet[i] > media:
        acima[i] += vet[i] 
print(f"Vetor: {vet}")
print(f"A média dos valores no vetor é: {media}")
print("Valores acima da média: ")
print(acima)