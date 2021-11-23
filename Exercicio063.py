'''Exercicio 063 Curso em Video Python Mundo 2
Escrever um programa que leia um N inteiro qualquer e mostre na tela estes N
primeiros termos da sequencia de Fibonacci'''
print('-'*30)
n = int(input('Digite quantos termos deseja ver em uma sequencia de Fibonacci: '))
print('-'*30)
cont = 3
a = 0
b = 1
c = 0
print('{} => {} '.format(a, b), end = '')
while cont <= n:
    c = a + b
    print('=> {} '.format(c), end = '')
    a = b
    b = c
    cont += 1
print('=> FIM')