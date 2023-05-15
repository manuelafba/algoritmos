menor = float('inf')
maior = float('-inf')

while True:
    valor = int(input("Digite um valor inteiro positivo (ou -1 para encerrar): "))
    
    if valor == -1:
        break
    
    if valor > maior:
        maior = valor
    
    if valor < menor:
        menor = valor

if menor == float('inf') or maior == float('-inf'):
    print("Não foram inseridos valores válidos.")
else:
    print(f"O menor valor do conjunto é: {menor}")
    print(f"O maior valor do conjunto é: {maior}")