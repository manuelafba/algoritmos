print("URNA ELETRÔNICA")

candidato1  = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulos = 0
brancos = 0

while True:
    voto = int(input("Digite o número do seu candidato (ou digite 5 para voto nulo ou 6 para voto em branco): "))
    if voto == 0:
        break

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto inválido!")
        continue

    totalvotos = candidato1 + candidato2 + candidato3 + candidato4 + nulos + brancos

print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Candidato 3: {candidato3} votos")
print(f"Candidato 4: {candidato4} votos")
print(f"{nulos} votos nulos")
print(f"{brancos} votos em branco")
print(f"Total de {totalvotos} votos")