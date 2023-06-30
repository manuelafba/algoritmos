sexo = input("Digite seu sexo:")
estado = input("Digite seu estado civil: ")
nome = input("Digite seu nome: ")

if estado == "casada" and sexo == "feminino":
    print("Sra." ,nome)
else:
    if estado == "casado" and sexo == "masculino":
        print("Sr." ,nome)
    else:
        if estado == "solteira" and sexo == "feminino":
            print("Srta." ,nome)
