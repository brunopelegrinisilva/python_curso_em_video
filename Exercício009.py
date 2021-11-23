"""
Exercício 009 => Curso em vídeo
Feito dia 26/02/2020
"""
num = int(input('Digite um número para ver sua tabuada: '))
i = 0
print('-'*12)
while (i<=10):
    print('{} x {:2}  = {}'.format(num,i,(num*i)))
    i += 1
print('-'*12)