Algoritmo "Estrutura de Dados Heterogêneos"
//  
//  
// Descrição   : Aula 11 - Algoritmos
// Autor(a)    : Manuela Araújo
// Data atual  : 15/06/2023
tipo
ficha = registro
nome: caractere
n1, n2, n3, media: real
fimregistro
Var
// Seção de Declarações das variáveis 
x: inteiro
soma: vetor [1..5] de real
media: vetor [1..5] de real
aluno: vetor [1..5] de ficha

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
para x de 1 ate 5 faca
escreva("Digite o nome do aluno: ")
leia(aluno[x].nome)
escreva("Digite a nota da primeira avaliação: ")
leia(aluno[x].n1)
escreva("Digite a nota da segunda avaliação: ")
leia(aluno[x].n2)
escreva("Digite a nota da terceira avaliação: ")
leia(aluno[x].n3)
soma[x] <- aluno[x].n1 + aluno[x].n2 + aluno[x].n3
media[x] <- soma[x] / 3
fimpara
limpatela

para x de 1 ate 5 faca
escreval("Aluno: ",aluno[x].nome," -- Nota 1ª AV: ",aluno[x].n1," -- Nota 2ª AV: ",aluno[x].n2," -- Nota 3ª AV: ",aluno[x].n3," -- Média final: ",media[x])
escreval("")
fimpara
Fimalgoritmo