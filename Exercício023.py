'''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

'''Metodo com string
num = str(input('Digite um numero entre 0 e 9999: '))
print('Analisando o numero {} '.format(num))
print('Unidade {} '.format(num[3]))
print('Dezena {} '.format(num[2]))
print('Centena {} '.format(num[1]))
print('Milhar {} '.format(num[0]))
Metodo com string
'''

# metodo com numero
num = int(input('Digite um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {} '.format(num))
print('Unidade {} '.format(u))
print('Dezena {} '.format(d))
print('Centena {} '.format(c))
print('Milhar {} '.format(m))