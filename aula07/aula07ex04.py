print("CARDÁPIO")
total = 0

while True:
    codigo = int(input("Digite o código do pedido: "))
    if codigo == 000:
        break

    quantidade = int(input("Digite a quantidade do pedido: "))

    if codigo == 100:
        valor = 1.20
        descricao = "Cachorro quente"
    elif codigo == 101:
        valor = 1.30
        descricao = "Bauru simples"
    elif codigo == 102:
        valor = 1.50
        descricao = "Bauru com ovo"
    elif codigo == 103:
        valor = 1.20
        descricao = "Hambúrguer"
    elif codigo == 104:
        valor = 1.30
        descricao = "Cheeseburguer"
    elif codigo == 105:
        valor = 1.00
        descricao = "Refrigerante"
    else:
        print("Código inválido")
        continue

    total += valor * quantidade

    print(f"{quantidade} x {descricao}")

print(f"Total do pedido: R$ {total}")


