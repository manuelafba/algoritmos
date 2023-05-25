Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/05/2023
Var
// Seção de Declarações das variáveis 
elemento : vetor[1..5, 1..5] de inteiro
i, j : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva("Digite o elemento ",i," da ",j,"ª linha: ")
leia(elemento[i ,j])
fimpara
fimpara
limpatela
para i de 1 ate 5 faca
para j de 1 ate 5 faca
escreva(elemento[i, j], " ")
fimpara
escreval("")
fimpara
para i de 1 ate 5 faca
para j de 1 ate 5 faca
se i = j entao
escreva(elemento[i, j]:4)
senao
escreva("--")
fimse
fimpara
escreval("")
fimpara

Fimalgoritmo