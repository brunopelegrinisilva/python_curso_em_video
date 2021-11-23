'''Exercicio 060 Curso em Video Python Mundo 2, executar fatorial'''
# minha solucao abaixo
'''num = int(input('Digite o numero que deseja realizar o fatorial: '))
fat = num
while num != 1:
    fat = fat * (num - 1)
    num -= 1
print('O fatorial do numero escolhido eh {}.'.format(fat))'''
# solucao guanabara
n = int(input('Digite o fatorial a ser calculado: '))
c = n
f = 1
print('Calculando {}! '.format(n), end ='')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' x ', end ='')
    f *= c
    c -= 1
print('{}'.format(f))