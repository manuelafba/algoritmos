from dataclasses import dataclass

@dataclass
class RegPaciente:
    id: int
    nome: str
    doenca: str
    idade: int

paciente = [None]*5
for i in range(5):
   paciente[i] = RegPaciente(0,'','',0)

soma=0
op=''

for i in range(5):
    print(f"{i+1}° Paciente")
    paciente[i].nome = input("Nome: ")
    paciente[i].doenca = input("Doença: ")
    paciente[i].id = int(input("Id: "))
    paciente[i].idade = int(input("Idade: "))

while op != "N":
    op = input("Deseja fazer alguma operação? Digite S para sim e N para não: ")
    if op == "S":
        acao = int(input("""
        [1] Buscar por ID
        [2] Atualizar doença de um paciente
        [3] Remover paciente da base de dados
        [4] Exibir a média das idades
        [5] Exibir todos os pacientes registrados
        Digite o número correspondente à ação que deseja realizar: """))

        if acao == 1:
            ID = int(input("Digite o ID do paciente: "))
            for i in range(5):
                if paciente[i].id == ID:
                    print(f"""
                    ID: {paciente[i].id}
                    Nome: {paciente[i].nome}
                    Doença: {paciente[i].doenca}
                    Idade: {paciente[i].idade}
                    """)
                if paciente[i].id == 0:
                    print("Paciente não encontrado")

        if acao == 2:
            ID = int(input("Digite o ID do paciente: "))
            for i in range(5):
                if paciente[i].id == ID:
                    paciente[i].doenca = input("Digite a nova doença do paciente: ")
                    print("Doença atualizada")
        
        if acao == 3:
            ID = int(input("Digite o ID do paciente que deseja remover: \n"))
            for i in range(5):
                if paciente[i].id == ID:
                    paciente[i] = RegPaciente(0,'','',0)
                    print("Paciente excluído")

        if acao == 4:
            for i in range (len(paciente)):
                if paciente[i].idade != 0:
                    soma += paciente[i].idade
            print(f'A média das idades é: {soma/5}')
        
        if acao == 5:
            print("PACIENTES REGISTRADOS: ")
            for paciente in paciente:
                if paciente.nome != '' and paciente.idade != 0:
                    print(f"""
                    ID: {paciente.id}
                    Nome: {paciente.nome}
                    Doença: {paciente.doenca}
                    Idade: {paciente.idade}
                    """)
        else:
            print("Ação inválida. Por favor, digite um número correspondente a uma ação válida.")

print("Programa Encerrado")