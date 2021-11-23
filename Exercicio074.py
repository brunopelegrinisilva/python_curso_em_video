'''Execicio 74 Mundo 3 Python Tuplas, CeV Guanabara
Crie um programa que gere 5 numeros aleatorios e coloque em uma tupla
depois mostre a listagem gerada e indique o menor e o maior valor presente na tupla'''
from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados foram {tupla}')
#print(f'O menor valor sorteado foi {sorted(tupla)[0]}') eu fiz assim
print(f'O menor valor sorteado foi {min(tupla)}') # metodo do Guanabara
#print(f'O maior valor sorteado foi {sorted(tupla)[-1]}') eu fiz assim
print(f'O maior valor sorteado foi {max(tupla)}') # metodo do Guanabara
