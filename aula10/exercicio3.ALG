Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Se��o de Declara��es das vari�veis 
matriz1 : vetor[1..5, 1..5] de inteiro
matriz2 : vetor[1..5, 1..5] de inteiro
valor, i, j : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva("Digite o elemento ",i," da ",j,"� linha: ")
leia(matriz1[i ,j])
fimpara
fimpara
escreva("Digite um valor: ")
leia(valor)
limpatela
para i de 1 ate 5 faca
para j de 1 ate 5 faca
matriz2[i, j] <- (matriz1[i, j] * valor)
escreva(matriz2[i, j], " ")
fimpara
escreval("")
fimpara


Fimalgoritmo