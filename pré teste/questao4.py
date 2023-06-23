from dataclasses import dataclass

n = int(input("Digite o número de livros: "))

@dataclass
class RegLivro:
    titulo: str
    autor: str
    ano: int

livro = [None] * n
for i in range(n):
    livro[i] = RegLivro('', '', 0)
    print(f"Livro {i+1}: ")
    livro[i].titulo = input("Digite o título do livro: ")
    livro[i].autor = input("Digite o autor do livro: ")
    livro[i].ano = input("Digite o ano de publicação do livro: ")
    
anoref = int(input("Digite o ano de referência: "))
print(f"Livros lançados antes de {anoref}")
for i in range(n):
    if int(livro[i].ano) < anoref:
        print(f"{livro[i].titulo} - {livro[i].autor}")