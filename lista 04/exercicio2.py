vetor = []
vetorpar = []
vetorimpar = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(numero)

    if numero % 2 == 0:
        vetorpar.append(numero)
    else:
        vetorimpar.append(numero)

vetorpar2 = sorted(vetorpar)
vetorimpar2 = sorted(vetorimpar, reverse=True)

print(vetor)
print(vetorpar2)
print(vetorimpar2)


    

