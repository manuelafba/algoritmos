Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor    : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Se��o de Declara��es das vari�veis
elemento : vetor[1..3, 1..3] de inteiro
soma, i, j : inteiro
media : real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
para i de 1 ate 3 faca
para j de 1 ate 3 faca
escreva("Digite o elemento ",i," da ",j,"� linha: ")
leia(elemento[i ,j])
soma <- soma + elemento[i, j]
media <- soma / 9
fimpara
fimpara
escreval("A soma de todos os elementos da matriz �: ",soma)
escreval("A m�dia de todos os elementos da matriz �: ",media)
Fimalgoritmo