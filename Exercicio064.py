'''Exercicio 064 Curso em Video Python Mundo 2
Fazer um programa que some os numeros digitados ate que atenda a condicao de 
parada 999'''
n = c = a = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    a += n
    c += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma deles eh {}.'.format(c, a))