'''Exercicio 062 Curso em video Python, Melhorar a PA do 061, perguntando se quer mais.'''
n = int(input('Digite o primeiro termo da PA: '))
f = int(input('Digite o fator da PA: '))
c = 1
t = 0
p = 10
while p != 0:
    t = t + p
    while c <= t:
        print('{} => '.format(n), end = '')
        n += f
        c += 1
    p = int(input(' Quantos termos mais quer ver? '))
print('Entao paramos por aqui! Mostramos um total de {} termos.'.format(c))