"""
Exercício 016 => Curso em vídeo
Curso Python #08 - Utilizando Módulos
Feito dia  /2020
"""
from math import trunc #dá pra importar math inteira e usar a função com math.trunc
num = float(input('Digite um número real: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

