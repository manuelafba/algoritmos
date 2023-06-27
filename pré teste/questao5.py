from dataclasses import dataclass

n = int(input("Digite a quantidade de alunos: "))

@dataclass
class RegAluno:
    nome: str
    nota: float

maiornota = 0
maiornome = ''

aluno = [None] * n
for i in range(n):
    aluno[i] = RegAluno('', 0)
    print(f"Aluno {i+1}: ")
    aluno[i].nome = input("Digite o nome do aluno: ")
    aluno[i].nota = float(input("Digite a nota do aluno: "))

    if i == 1:
        maiornota = aluno[i].nota
        maiornome = aluno[i].nome
    else: 
        if aluno[i].nota > maiornota:
            maiornota = aluno[i].nota
            maiornome = aluno[i].nome

print("Alunos: ")
for i in range(n):
    print(f"Nome: {aluno[i].nome} | Nota: {aluno[i].nota}")
print('')
print("Aluno com a maior nota: ")
print(f"Nome: {maiornome} | Nota: {maiornota}")