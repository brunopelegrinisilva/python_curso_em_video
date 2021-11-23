"""
Exercício 017 => Curso em vídeo
Curso Python #08 - Utilizando Módulos
Feito dia  08/03/2020
"""
#método matemático
#oposto = float(input('Digite o valor do cateto oposto: '))
#adjacente = float(input('Digite o valor do cateto adjacente: '))
#hipotenusa = (((oposto ** 2)+(adjacente ** 2)) ** 0.5)
#print('O valor do cateto oposto é: {} \nO valor do cateto adjacente é: {} \nO valor da hipotenusa é: {:.3f}'.format(oposto, adjacente, hipotenusa))

import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('O valor do cateto oposto é: {} \nO valor do cateto adjacente é: {} \nO valor da hipotenusa é: {:.3f}'.format(oposto, adjacente, hipotenusa))