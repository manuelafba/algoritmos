matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):  # linha
    for c in range(3):  # coluna
        matriz1[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da primeira matriz: '))

for l in range(3):  # linha
    for c in range(3):  # coluna
        matriz2[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da segunda matriz: '))

for l in range(3): #linhas
    for c in range(3): #colunas
        for k in range(3): #colunas e linhas
            resultado[l][c] += matriz1[l][k] * matriz2[k][c]

for l in range(3):
    for c in range(3):
        print(f'{matriz1[l][c]}', end=' ')
    print('')

for l in range(3):
    for c in range(3):
        print(f'{resultado[l][c]}', end=' ')
    print('')