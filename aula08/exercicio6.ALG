Algoritmo "semnome"
//  
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2023
Var
// Se��o de Declara��es das vari�veis 
A: vetor[1..20] de inteiro
i, aux: inteiro
inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
para i de 1 ate 20 faca
escreva("Digite o ",i," � valor: ")
leia (A[i])
fimpara
para i de 1 ate 10 faca
aux<-A[i]
A[i]<-A[21-i]
A[21-i]<-aux
fimpara
para i de 1 ate 20 faca
escreva(A[i], " ")
fimpara
Fimalgoritmo


