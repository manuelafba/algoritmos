Algoritmo "semnome"
//  
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2023
Var
// Seção de Declarações das variáveis 
n : vetor[1..20] de inteiro
p, m, x: inteiro
posi: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para p de 1 ate 20 faca
escreva("Digite o",p," º número: ")
leia(n[p])
se p = 1 entao
m <- n[p]
senao
se n[p] < m entao
m <- n[p]
posi <- p
fimse
fimse
fimpara
escreva("O menor valor é",m," na posição ",posi)
Fimalgoritmo
