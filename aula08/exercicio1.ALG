Algoritmo "semnome"
//  
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2023
Var
// Seção de Declarações das variáveis 
x, soma : inteiro
a : vetor[1..5] de inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
soma <- 0
para x de 1 ate 5 faca
escreva("Digite o ",x," º número: ")
leia(a[x])
fimpara

para x <- 1 ate 5 faca
se x % 2 <> 0 entao
soma <- soma + a[x]
fimse
fimpara

escreva("A soma dos números em posições ímpares é",soma)
Fimalgoritmo