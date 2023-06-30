num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print('O número' ,num, 'é divisível por 2')
elif num % 5 == 0:
    print('O número' ,num, 'é divisível por 5')
else:
    print('O número' ,num, 'não é divisível por 2 nem por 5')