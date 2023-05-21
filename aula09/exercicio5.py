while True:
    n = int(input("Digite o valor de n (Deve ser maior que 1): "))
    if n < 1: 
        print("Você digitou um valor inválido")
        continue
    b = int(input("Digite o valor de b (Deve ser maior ou igual a 2): "))
    if b < 2:
        print("Você digitou um valor inválido")
        continue
    else:
        break
resultado = b**n
print(f"O resultado da potenciação é {resultado}")    