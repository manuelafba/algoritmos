Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor    : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Seção de Declarações das variáveis
matriz : vetor[1..3, 1..4] de inteiro
matrizt : vetor[1..4, 1..3] de inteiro
i, j: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para i de 1 ate 3 faca
para j de 1 ate 4 faca
escreva("Digite o elemento ",i," da ",j,"ª linha: ")
leia(matriz[i ,j])
fimpara
fimpara

limpatela
escreval("Matriz inicial: ")
para i de 1 ate 3 faca
para j de 1 ate 4 faca
escreva(matriz[i, j], " ")
fimpara
escreval("")
fimpara

escreval("Matriz transposta: ")
para j de 1 ate 4 faca
para i de 1 ate 3 faca
matrizt[j, i] <- matriz[i, j]
escreva(matrizt[j, i], " ")
fimpara
escreval("")
fimpara


Fimalgoritmo