Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Se��o de Declara��es das vari�veis 
elemento : vetor[1..5, 1..5] de inteiro
i, j : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva("Digite o elemento ",i," da ",j,"� linha: ")
leia(elemento[i ,j])
fimpara
fimpara
limpatela
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva(elemento[i, j], " ")
fimpara
escreval("")
fimpara
para i de 1 ate 5 faca
para j de 1 ate 5 faca
se i = j entao
escreva(elemento[i, j]:4)
senao
escreva("--")
fimse
fimpara
escreval("")
fimpara

Fimalgoritmo