Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Seção de Declarações das variáveis 
elemento : vetor[1..5, 1..5] de inteiro
soma, i, j : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva("Digite o elemento ",i," da ",j,"ª linha: ")
leia(elemento[i ,j])
soma <- soma + elemento[i, j]
fimpara
fimpara
escreva("A soma de todos os elementos da matriz é: ",soma)

Fimalgoritmo