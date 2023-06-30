salario = int(input('Digite o salário bruto do funcionário: '))

if salario < 300:
    salarioliq = salario - salario*0.95
elif salario <= 1200:
    salarioliq = salario - salario*0.90
elif salario > 1200:
    salarioliq = salario - salario*0.85
    print(salarioliq)