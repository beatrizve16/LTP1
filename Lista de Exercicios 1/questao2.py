'''Exercício 2: Dada a tupla turma = ('André', 'Fernanda', 'Luiz'),
peça ao usuário para digitar o nome de um aluno. 
Cheque se o aluno está na tupla e exiba uma mensagem adequada.'''



turma = ('André', 'Fernanda', 'Luiz')

nome = input("Digite o nome de um aluno: ")

if nome in turma:
    print(nome + " está na turma")
else:
    print(nome + " não está na turma")
