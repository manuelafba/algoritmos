n = int(input("Digite o tamanho da matriz: "))

mat = [[0 for m in range(n)] for m in range(n)]
diag = [[0 for m in range(n)] for m in range(n)]

for l in range(n):
    for c in range(n):
        mat[l][c] = int(input(f"Digite o {c+1}º número da {l+1}º linha: "))
        if l == c:
            diag[l][c] += mat[l][c]

for l in range(n):
    for c in range(n):
        print(f"[{mat[l][c]}]", end='')
    print('')

if mat == diag:
    print("Diagonal")
else:
    print("Não é diagonal")