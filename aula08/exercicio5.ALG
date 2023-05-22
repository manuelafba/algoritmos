Algoritmo "semnome"
//  
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2023
Var
// Seção de Declarações das variáveis 
v1 : vetor[1..10] de real
v2 : vetor[1..10] de real
v3 : vetor[1..10] de real
i: inteiro
soma : real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para i de 1 ate 10 faca
escreva("Digite o",i," º número do vetor 1: ")
leia(v1[i])
fimpara
para i de 1 ate 10 faca
escreva("Digite o",i," º número do vetor 2: ")
leia(v2[i])
fimpara
para i de 1 ate 10 faca
v3[i] <- v1[i] + v2[i]
escreva("v3[" ,i, "] = ",v3[i])
fimpara
Fimalgoritmo

