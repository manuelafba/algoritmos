import random

mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]]

for c in range(10):  # coluna
    for l in range(10):  # linha
        mat[l][c] = random.randint(0, 9)

print("Matriz:")
for l in range(10):  
    for c in range(10):  
        print(f'[{mat[l][c]}]', end='')
    print('')

print("Diagonal principal:")
diagonal = []
for i in range(10):
    diagonal.append(mat[i][i])
    print(diagonal)