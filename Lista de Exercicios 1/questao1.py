'''Exercício 1: Peça ao usuário que insira um número.
Se o número for par, exiba "Número par". 
Se for ímpar, exiba "Número ímpar".'''


numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("número par")
else:
    print("número ímpar")
