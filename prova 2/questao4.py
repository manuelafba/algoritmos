from dataclasses import dataclass

n = int(input("Digite o número de filmes: "))

@dataclass 
class RegFilme:
    titulo: str
    diretor: str
    ano: int

filme = [None] * n

for i in range(n):
    filme[i] = RegFilme('', '', 0)
    print(f"Filme {i+1}")
    filme[i].titulo = input("Digite o título do filme: ")
    filme[i].diretor = input("Digite o diretor do filme: ")
    filme[i].ano = int(input("Digite o ano de lançamento do filme: "))

anoref = int(input("Digite o ano de referência: "))

for i in range(n):
    if anoref > filme[i].ano:
        print(f"Filmes lançados antes de {anoref}")
        print(f"{filme[i].titulo} - {filme[i].diretor} - {filme[i].ano}")