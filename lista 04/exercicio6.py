mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
cont = 0

for c in range(4):  # coluna
    for l in range(4):  # linha
        mat[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da matriz: '))
        if mat[l][c] > 10:
            cont +=1

for l in range(4):  # linha
    for c in range(4):  # coluna
        print(f'[{mat[l][c]}]', end='')
    print('')

print(f"O número de elementos maiores que 10 na matriz é {cont}")