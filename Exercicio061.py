'''Exercicio 061 Curso em video Python, criar uma PA e mostrar os 10 primeiros numeros.'''
n = int(input('Digite o primeiro termo da PA: '))
f = int(input('Digite o fator da PA: '))
c = 0
while c < 10:
    print('{}'.format(n), end = '')
    print(' => ' if c < 9 else ' e por ai vai...', end = '')
    n = n + f
    c += 1
print(' FIM!')