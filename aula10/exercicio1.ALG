Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Se��o de Declara��es das vari�veis 
elemento : vetor[1..5, 1..5] de inteiro
soma, i, j : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva("Digite o elemento ",i," da ",j,"� linha: ")
leia(elemento[i ,j])
soma <- soma + elemento[i, j]
fimpara
fimpara
escreva("A soma de todos os elementos da matriz �: ",soma)

Fimalgoritmo