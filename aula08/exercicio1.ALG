Algoritmo "semnome"
//  
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2023
Var
// Se��o de Declara��es das vari�veis 
x, soma : inteiro
a : vetor[1..5] de inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
soma <- 0
para x de 1 ate 5 faca
escreva("Digite o ",x," � n�mero: ")
leia(a[x])
fimpara

para x <- 1 ate 5 faca
se x % 2 <> 0 entao
soma <- soma + a[x]
fimse
fimpara

escreva("A soma dos n�meros em posi��es �mpares �",soma)
Fimalgoritmo