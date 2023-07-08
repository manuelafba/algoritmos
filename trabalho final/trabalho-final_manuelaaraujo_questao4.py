from dataclasses import dataclass

@dataclass
class RegVeiculo:
    id: int
    marca: str
    modelo: str
    preco: int

veiculo = [None]*5
for i in range(5):
   veiculo[i] = RegVeiculo(0,'','',0)

soma=0
op=''

for i in range(5):
    print(f"{i+1}° veículo")
    veiculo[i].id = int(input("ID: "))
    veiculo[i].marca = input("Marca: ")
    veiculo[i].modelo = input("Modelo: ")
    veiculo[i].preco = int(input("Preço: "))

while op != "N":
    op = input("Deseja fazer alguma operação? Digite S para sim e N para não: ")
    if op == "S":
        acao = int(input("""
        [1] Buscar por ID
        [2] Atualizar preço de um veículo
        [3] Remover veículo da base de dados
        [4] Exibir todos os veículos registrados
        Digite o número correspondente à ação que deseja realizar: """))

        if acao == 1:
            ID = int(input("Digite o ID do veículo: "))
            for i in range(5):
                if veiculo[i].id == ID:
                    print(f"""
                    ID: {veiculo[i].id}
                    Marca: {veiculo[i].marca}
                    Modelo: {veiculo[i].modelo}
                    Preço: R${veiculo[i].preco}
                    """)
                if veiculo[i].id == 0:
                    print("Veículo não encontrado")

        if acao == 2:
            ID = int(input("Digite o ID do veículo: "))
            for i in range(5):
                if veiculo[i].id == ID:
                    veiculo[i].preco = input("Digite o novo preço do veículo: ")
                    print("Preço atualizado")
        
        if acao == 3:
            ID = int(input("Digite o ID do veículo que deseja remover: \n"))
            for i in range(5):
                if veiculo[i].id == ID:
                    veiculo[i] = RegVeiculo(0,'','',0)
                    print("Veículo excluído")
        
        if acao == 4:
            print("VEÍCULOS REGISTRADOS: ")
            for veiculo in veiculo:
                if veiculo.marca != '' and veiculo.preco != 0:
                    print(f"""
                    ID: {veiculo.id}
                    Marca: {veiculo.marca}
                    Modelo: {veiculo.modelo}
                    Preço: R${veiculo.preco}
                    """)
        else:
            print("Ação inválida. Por favor, digite um número correspondente a uma ação válida.")

print("Programa Encerrado")