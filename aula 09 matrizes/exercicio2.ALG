Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor    : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Se��o de Declara��es das vari�veis
elemento : vetor[1..4, 1..4] de inteiro
soma, i, j : inteiro
media : real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
para i de 1 ate 4 faca
para j de 1 ate 4 faca
escreva("Digite o elemento ",i," da ",j,"� linha: ")
leia(elemento[i ,j])
soma <- soma + elemento[i, j]
fimpara
fimpara
limpatela

para i de 1 ate 4 faca
para j de 1 ate 4 faca
escreva(elemento[i, j], " ")
fimpara
escreval("")
fimpara
para i de 1 ate 4 faca
para j de 1 ate 4 faca
se i = j entao
escreva(elemento[i, j]:4)
senao
escreva("--")
fimse
fimpara
escreval("")
fimpara
escreval("A soma dos elementos da matriz � :",soma)
Fimalgoritmo