mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
somalinhas = []
somacolunas = []

for c in range(5):  # coluna
    for l in range(5):  # linha
        mat[l][c] = int(input(f'Digite o {l + 1}º elemento da {c + 1}ª coluna da matriz: '))

print("Matriz:")
for l in range(5):  
    for c in range(5):  
        print(f'[{mat[l][c]}]', end='')
    print('')

# soma linha
for l in range(5):
    somal = 0
    for c in range(5):
        somal += mat[l][c]
    somalinhas.append(somal)
    if somal % 2 == 0:
        print(f"A soma dos elementos da linha {l+1} é {somal} e par")
    else:
        print(f"A soma dos elementos da linha {l+1} é {somal} e ímpar")

# soma colunas
for c in range(5):
    somac = 0
    for l in range(5):
        somac += mat[l][c]
    somacolunas.append(somac)
    if somac % 2 == 0:
        print(f"A soma dos elementos da coluna {c+1} é {somac} e par")
    else:
        print(f"A soma dos elementos da coluna {c+1} é {somac} e ímpar")


