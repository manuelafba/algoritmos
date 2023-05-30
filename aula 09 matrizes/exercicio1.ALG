Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor    : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Seção de Declarações das variáveis
elemento : vetor[1..3, 1..3] de inteiro
soma, i, j : inteiro
media : real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para i de 1 ate 3 faca
para j de 1 ate 3 faca
escreva("Digite o elemento ",i," da ",j,"ª linha: ")
leia(elemento[i ,j])
soma <- soma + elemento[i, j]
media <- soma / 9
fimpara
fimpara
escreval("A soma de todos os elementos da matriz é: ",soma)
escreval("A média de todos os elementos da matriz é: ",media)
Fimalgoritmo