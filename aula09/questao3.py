maior = 0
menor = 0
i = 0
while True:
    idade = int(input("Digite a idade da pessoa: "))
    if idade == 0:
        break
    
    if idade > 18:
        menor += 1
    elif idade < 60:
        maior += 1
    else:
        i += 1
    
print(f"A a quantidade de pessoas com idade inferior a 18 é {menor} e a de pessoas com idade superior a 60 é {maior}")