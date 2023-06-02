from random import randint

vetor1 = []
vetor2 = []
vetorsoma = []
vetordif = []
vetorprod = []

for i in range(10):
    vetor1.append(randint(0, 10))
    vetor2.append(randint(0, 10))
    vetorsoma.append(vetor1[i] + vetor2[i])
    vetordif.append(vetor1[i] - vetor2[i])
    vetorprod.append(vetor1[i] * vetor2[i])

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Soma: {vetorsoma}")
print(f"Diferença: {vetordif}")
print(f"Produto: {vetorprod}")
