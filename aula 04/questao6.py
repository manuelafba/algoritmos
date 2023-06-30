ano = int(input("Digite seu ano de nascimento: "))
anoat = int(input("Digite o ano atual: "))
idade = anoat - ano

if idade < 16:
    print("Você não está apto a votar ou dirigir")
elif 16 <= idade < 18:
    print("Voce está apto a votar, mas não está apto a dirigir")
else:
    print("Você está apto a votar e dirigir") 