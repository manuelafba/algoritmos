Algoritmo "Aula 11 - Ex 4"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descri��o   : Aula 11 - Exerc�cio 4
// Autor(a)    : Manuela Ara�jo
// Data atual  : 15/06/2023
tipo
ficha = registro
nome: caractere
func: caractere
sal, salfinal: real
fimregistro
Var
// Se��o de Declara��es das vari�veis
x: inteiro
sal: vetor[1..3] de real
salfinal: vetor[1..3] de real
funcionario: vetor [1..3] de ficha

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
para x de 1 ate 3 faca
escreva("Digite o nome do funcion�rio: ")
leia(funcionario[x].nome)
escreva("Digite a fun��o do funcion�rio: ")
leia(funcionario[x].func)
escreva("Digite o sal�rio do funcion�rio: ")
leia(funcionario[x].sal)

salfinal[x] <- funcionario[x].sal * 1.3
fimpara
limpatela

escreval("==CONTRACHEQUE==")
para x de 1 ate 3 faca
escreval("Nome: ",funcionario[x].nome)
escreval("Fun��o: ",funcionario[x].func)
escreval("Sal�rio: R$",funcionario[x].sal)
escreval("Sal�rio com aumento: R$",salfinal[x])
escreval("")
fimpara
Fimalgoritmo