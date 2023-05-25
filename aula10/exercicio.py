vet = [0]*10
par = [0]*10
impar = [0]*10

for i in range (0, 10):
    vet[i] = int(input(f"Digite o {i + 1}º valor: "))
    if i % 2 == 0:
        par[i] += vet[i]
    else:
        impar[i] += vet[i]

print(par)
print(impar)