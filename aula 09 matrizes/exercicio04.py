matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):  # linha
    for c in range(3):  # coluna
        matriz[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da matriz: '))

for l in range(len(matriz)): #linhas
    for c in range(len(matriz)): #colunas
        for k in range(len(matriz)): #colunas e linhas
            resultado[l][c] += matriz[l][k] * matriz[k][c]

for l in range(3):  
    for c in range(3):  
        print(f'[{resultado[l][c]}]', end='')
    print('')