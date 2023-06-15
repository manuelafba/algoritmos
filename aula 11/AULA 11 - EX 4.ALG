Algoritmo "Aula 11 - Ex 4"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aula 11 - Exercício 4
// Autor(a)    : Manuela Araújo
// Data atual  : 15/06/2023
tipo
ficha = registro
nome: caractere
func: caractere
sal, salfinal: real
fimregistro
Var
// Seção de Declarações das variáveis
x: inteiro
sal: vetor[1..3] de real
salfinal: vetor[1..3] de real
funcionario: vetor [1..3] de ficha

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para x de 1 ate 3 faca
escreva("Digite o nome do funcionário: ")
leia(funcionario[x].nome)
escreva("Digite a função do funcionário: ")
leia(funcionario[x].func)
escreva("Digite o salário do funcionário: ")
leia(funcionario[x].sal)

salfinal[x] <- funcionario[x].sal * 1.3
fimpara
limpatela

escreval("==CONTRACHEQUE==")
para x de 1 ate 3 faca
escreval("Nome: ",funcionario[x].nome)
escreval("Função: ",funcionario[x].func)
escreval("Salário: R$",funcionario[x].sal)
escreval("Salário com aumento: R$",salfinal[x])
escreval("")
fimpara
Fimalgoritmo