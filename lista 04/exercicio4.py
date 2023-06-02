mat1 = [[0, 0, 0] , [0, 0, 0]]
mat2 = [[0, 0, 0] , [0, 0, 0]]
soma = [[0, 0, 0] , [0, 0, 0]]

for c in range(3): #coluna
    for l in range(2): #linha
        mat1[l][c] = int(input(f'Digite o {l+1}º elemento da {c+1}ª coluna da matriz 1: '))

for c in range(3): #coluna
    for l in range(2): #linha
        mat2[l][c] = int(input(f'Digite o {l+1}º elemento da {c+1}ª coluna da matriz 2: '))
        soma[l][c] = (mat1[l][c] + mat2[l][c])

for c in range(3): #coluna
    for l in range(2): #linha
        print(f'[{soma[l][c]}]', end='')
    print('')