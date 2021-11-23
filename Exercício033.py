# Exercício Python 033: Faça um programa que leia três números e 
# mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeito valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# verifica o menor valor, assumindo a uma variavel como menor e testando as outras no if
menor = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
# verifica o maior valor, assumindo uma variavel como maior e testando as outras no if
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor numero digitado eh {} '.format(menor))
print('O maior numero digitado eh {} '.format(maior))