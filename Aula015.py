'''Aula 015 - Curso em Video Python Mundo 2
Lacos de Repeticao, Parte 3
Break e Loopings Infinitos'''
n = 0
while True:
    print(f'{n} ', end = '')
    n += 1
    if n == 10:
        break
print('Finito.')