Algoritmo "semnome"
//  
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2023
Var
// Seção de Declarações das variáveis 
A: vetor[1..20] de inteiro
i, aux: inteiro
inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para i de 1 ate 20 faca
escreva("Digite o ",i," º valor: ")
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


