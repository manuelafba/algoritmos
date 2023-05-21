total = 0
totalquadrados = 64
graos = 1
quadrado = 1

while quadrado <= totalquadrados:
    total += graos
    graos *= 2
    quadrado += 1

print(f"O monge vai receber {total} grãos") 