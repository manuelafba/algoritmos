num = int(input('Digite um número inteiro: '))

if num < 2:
    print(f'O número {num} não é primo')
else:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(f'O número {num} é primo')
        exit()

    print(f'O número {num} não é primo')