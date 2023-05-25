Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Seção de Declarações das variáveis 
matriz1 : vetor[1..5, 1..5] de inteiro
matriz2 : vetor[1..5, 1..5] de inteiro
valor, i, j : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva("Digite o elemento ",i," da ",j,"ª linha: ")
leia(matriz1[i ,j])
fimpara
fimpara
escreva("Digite um valor: ")
leia(valor)
limpatela
para i de 1 ate 5 faca
para j de 1 ate 5 faca
matriz2[i, j] <- (matriz1[i, j] * valor)
escreva(matriz2[i, j], " ")
fimpara
escreval("")
fimpara


Fimalgoritmo