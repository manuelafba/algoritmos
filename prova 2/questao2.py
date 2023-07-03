vet = [0]*5
valorx = [0]*5
soma = [0]*5
sub = [0]*5
mult = [0]*5
div = [0]*5

for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor do vetor: "))
    vet[i] += valor 

x = int(input("Digite um valor qualquer: "))

for i in range(5):
    valorx[i] += x

for i in range(5):
    soma[i] = vet[i] + valorx[i]
    sub[i] = vet[i] - valorx[i]
    mult[i] = vet[i] * valorx[i]
    div[i] = vet[i] / valorx[i]


print(f"Vetor: {vet}")
print(f"Valor: {x}")
print(f"Soma: {soma}")
print(f"Diferença: {sub}")
print(f"Produto: {mult}")
print(f"Divisão: {div}")
