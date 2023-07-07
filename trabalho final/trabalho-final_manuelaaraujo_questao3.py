matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizSoma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for l in range(3):  # linha
    for c in range(3):  # coluna
        matriz[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da matriz: '))
    

for i in range(3):
    for j in range(3):
        for l in range(i + 1):
            for c in range(j + 1):
                soma += matriz[l][c]
        
        matrizSoma[i][j] = soma

for l in range(3):  
    for c in range(3):  
        print(f'[{matrizSoma[l][c]}]', end='')
    print('')
