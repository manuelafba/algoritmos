Algoritmo "Aula 11 - Ex 1"
//
//
// Descri��o   : Aula 11 - Algoritmos
// Autor(a)    : Manuela Ara�jo
// Data atual  : 15/06/2023
tipo
ficha = registro
nome: caractere
n1, n2, n3, media: real
fimregistro
Var
// Se��o de Declara��es das vari�veis
x: inteiro
soma: vetor [1..5] de real
media: vetor [1..5] de real
aluno: vetor [1..5] de ficha

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
para x de 1 ate 5 faca
escreva("Digite o nome do aluno: ")
leia(aluno[x].nome)
escreva("Digite a nota da primeira avalia��o: ")
leia(aluno[x].n1)
escreva("Digite a nota da segunda avalia��o: ")
leia(aluno[x].n2)
escreva("Digite a nota da terceira avalia��o: ")
leia(aluno[x].n3)
soma[x] <- aluno[x].n1 + aluno[x].n2 + aluno[x].n3
media[x] <- soma[x] / 3
fimpara
limpatela

para x de 1 ate 5 faca
escreval("Aluno: ",aluno[x].nome)
escreval("Nota 1� AV: ",aluno[x].n1)
escreval("Nota 2� AV: ",aluno[x].n2)
escreval("Nota 3� AV: ",aluno[x].n3)
escreval("M�dia final: ",media[x])
escreval("")
fimpara
Fimalgoritmo