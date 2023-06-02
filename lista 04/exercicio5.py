mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
soma = 0

for c in range(5):  # coluna
    for l in range(5):  # linha
        mat[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da matriz: '))

print("Matriz:")
for l in range(5):  # linha
    for c in range(5):  # coluna
        print(f'[{mat[l][c]}]', end='')
    print('')

print("Diagonal secundária:")
for i in range(len(mat)):
    print(mat[i][len(mat) - i - 1])
    soma += mat[i][len(mat) - i - 1]

print(f"Soma dos elementos: {soma}")