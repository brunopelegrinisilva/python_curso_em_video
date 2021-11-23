"""
Exercício 018 => Curso em vídeo
Curso Python #08 - Utilizando Módulos
Feito dia  08/03/2020
"""
import math
ang = float(input('Digite o valor de um angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo digitado foi {}\nSeu seno é {:.2f} \nSeu cosseno é {:.2f} \nSua tangente é {:.2f}'.format(ang, sen, cos, tan))
