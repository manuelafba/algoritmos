maior = 0
menor = 0
meio = 0
while True:
    idade =  int(input("Digite a idade da pessoa: "))
    if idade == 0:
        break
    if idade > 60:
        maior += 1
    elif idade < 18:
        menor += 1
    else:
        meio += 1

print(f"A quantidade de pessoas com idade superior a 60 é {maior} e {menor} com idade inferior a 18")
