soma = 0
valores = 0

while True:
    valor = int(input("Digite um valor inteiro positivo (ou um valor negativo para cancelar): "))
    
    if valor < 0:
        break
    
    soma += valor
    valores += 1

if valores == 0:
    print("Nenhum valor válido foi inserido.")
else:
    media = soma / valores
    print("A média dos valores digitados é:", media)