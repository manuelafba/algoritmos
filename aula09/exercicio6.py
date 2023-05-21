soma = 1
n = int(input("Digte um número: "))

for i in range (1, n):
    n2 = 1 / (i+1)
    soma = soma + n2

print(f"A soma é {soma}")
