Algoritmo "Aula 11 - Ex 2"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descri��o   : Aula 11 - Exerc�cio 2
// Autor(a)    : Manuela Ara�jo
// Data atual  : 15/06/2023
tipo
ficha = registro
mat: inteiro
nome: caractere
curso: caractere
disc: caractere
n1, n2, media: real
fimregistro
Var
// Se��o de Declara��es das vari�veis
x: inteiro
soma: vetor [1..10] de real
media: vetor [1..10] de real
aluno: vetor [1..10] de ficha

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
para x de 1 ate 10 faca
escreva("Digite o nome do aluno: ")
leia(aluno[x].nome)
escreva("Digite a matricula do aluno: ")
leia(aluno[x].mat)
escreva("Digite o curso do aluno: ")
leia(aluno[x].curso)
escreva("Digite a disciplina: ")
leia(aluno[x].disc)
escreva("Digite a primeira nota: ")
leia(aluno[x].n1)
escreva("Digite a segunda nota: ")
leia(aluno[x].n2)

soma[x] <- aluno[x].n1 + aluno[x].n2
media[x] <- soma[x] / 2
fimpara
limpatela

para x de 1 ate 10 faca
escreval("Aluno: ",aluno[x].nome)
escreval("Matr�cula: ",aluno[x].mat)
escreval("Curso: ",aluno[x].curso)
escreval("Disciplina: ",aluno[x].disc)
escreval("Nota 1: ",aluno[x].n1)
escreval("Nota 2: ",aluno[x].n2)
escreval("M�dia final : ",media[x])
escreval("")
fimpara
Fimalgoritmo