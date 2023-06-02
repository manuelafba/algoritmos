vetor = []
vetor2 = []

for i in range(10):
    while True:
        numero = int(input(f"Digite o {i+1} valor (deve ser positivo): "))
        if numero >= 0:
            break
        else:
            print("Você digitou um número negativo.")
    vetor.append(numero)

for i in range(10):
    if i % 2 == 0:
        novovalor = vetor[i] / 2
    else:
        novovalor = vetor[i] * 3
    vetor2.append(novovalor)

print(vetor)
print(vetor2)
