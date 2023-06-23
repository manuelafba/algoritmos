n = int(input("Digite um número inteiro: "))

matriz = [[0 for m in range(n)] for m in range(n)]
id = [[0 for m in range(n)] for m in range(n)]

for l in range(n):
    for c in range(n):
        matriz[l][c] = int(input(f"Escreva o {c+1}º elemento da {l+1}ª linha: "))
        if l == c:
            id[l][c] += 1
            
for l in range(n):
    for c in range(n):
        print(f'[{matriz[l][c]}]', end='')
    print('')

if matriz == id:
    print("Matriz identidade")
else:
    print("Não é matriz identidade")