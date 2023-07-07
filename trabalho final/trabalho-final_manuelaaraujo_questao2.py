n = int(input("Digite o tamanho da matriz (N x N): "))

matriz = [[0] * n for _ in range(n)] # Inicializar a matriz com zeros

valor = 1 # Valor inicial
inicioLinha, inicioColuna = 0, 0
fimLinha, fimColuna = n - 1, n - 1

while inicioLinha <= fimLinha and inicioColuna <= fimColuna:
    for c in range(inicioColuna, fimColuna + 1): # c = coluna
        matriz[inicioLinha][c] = valor
        valor += 1
    inicioLinha += 1

    for l in range(inicioLinha, fimLinha + 1): # l = linha
        matriz[l][fimColuna] = valor
        valor += 1
    fimColuna -= 1

    if inicioLinha <= fimLinha:
        for c in range(fimColuna, inicioColuna - 1, -1):
            matriz[fimLinha][c] = valor
            valor += 1
        fimLinha -= 1

    if inicioColuna <= fimColuna:
        for l in range(fimLinha, inicioLinha - 1, -1):
            matriz[l][inicioColuna] = valor
            valor += 1
        inicioColuna += 1

for l in matriz:
    print(l)
