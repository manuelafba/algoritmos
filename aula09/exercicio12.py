from random import randint

vet = [0] * 50
soma = desvio = 0

for i in range(50):
    vet[i] = randint(1, 5)
    soma += vet[i]

lista_ordenada = sorted(vet)
alturas = len(vet)

for i in range(50):
    desvio += (((vet[i] - (soma / 50)) ** 2) / 50) ** 0.5

if alturas % 2 == 1:
    mediana = lista_ordenada[alturas // 2]
else:
    meio1 = lista_ordenada[alturas // 2]
    meio2 = lista_ordenada[(alturas // 2) - 1]
    mediana = (meio1 + meio2) / 2

print(f'Alturas: {vet}')
print(f'A média das alturas é {soma/50}')
print(f'O desvio padrão das alturas é {desvio}')
print(f'A mediana é {mediana}')
