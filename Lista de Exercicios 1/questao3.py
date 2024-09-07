'''Exercício 3: Escreva um programa que imprima os primeiros
10 números da sequência de Fibonacci.'''


num = 10

a=0
b = 1

print(" primeiros 10 números da sequência de Fibonacci")
for _ in range(num):
    print(a)
    temp = a
    a = b
    b = temp + b
