idade = int(input("Digite sua idade:"))

if idade >= 5 and idade <= 7:
    print("Categoria infantil A")
elif idade <= 10:
    print("Categoria infantil B")
elif idade <= 13:
    print("Categoria juvenil A")
elif idade <= 17:
    print("Categoria juvenil B")
elif idade >= 18:
    print("Categoria adulto")
