Algoritmo "semnome"
//  
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/05/2023
Var
// Se��o de Declara��es das vari�veis 
n : vetor[1..20] de inteiro
p, m, x: inteiro
posi: inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
para p de 1 ate 20 faca
escreva("Digite o",p," � n�mero: ")
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
escreva("O menor valor �",m," na posi��o ",posi)
Fimalgoritmo
