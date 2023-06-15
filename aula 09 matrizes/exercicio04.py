matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(3):  # coluna
    for l in range(3):  # linha
        matriz[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da matriz: '))

for i in range(len(matriz)): #linhas
    for j in range(len(matriz)): #colunas
        for k in range(len(matriz)): #colunas e linhas
            resultado[i][j] += matriz[i][k] * matriz[k][j]

for l in range(3):  
    for c in range(3):  
        print(f'[{resultado[l][c]}]', end='')
    print('')