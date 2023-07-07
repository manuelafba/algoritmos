n = int(input("Digite o tamanho do vetor: "))
vet = []
pares = []

for i in range(n):
    num = int(input(f"Digite o {i+1}º número do vetor: "))
    vet.append(num)

alvo = int(input("Digite o número alvo: "))

for i in range(n):
    for j in range(i+1, n):
        if vet[i] + vet[j] == alvo:
            pares.append((vet[i], vet[j]))

print(f"Vetor: {vet}")
print(f"Pares: {pares}")