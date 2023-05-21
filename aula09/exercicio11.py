notas = []

for i in range(50):
    nota = float(input("Digite a nota {}: ".format(i + 1)))
    notas.append(nota)

soma = 0
for nota in notas:
    soma += nota
media = soma / 50
print(f"A média das notas é {media}")