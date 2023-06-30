numero = int(input("Digite um número de 4 algarismos: "))

dezena1 = (numero // 100) 
dezena2 = (numero - dezena1*100)

if numero^(1/2) == dezena1 + dezena2:
    print(f"A raiz quadrada de {numero} é igual a soma de suas dezenas")

