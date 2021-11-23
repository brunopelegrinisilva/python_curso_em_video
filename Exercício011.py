"""
Exercício 006 => Curso em vídeo
Feito dia 26/02/2020
"""
l = float(input('Digite a Largura da parede em metros: '))
a = float(input('Digite a Altura da parede em metros: '))
area = a * l
tinta = area / 2
print('Sua parede tem dimensões de {:.2f} x {:.2f} metros e sua área de {:.2f} m².'.format(a,l,area))
print('Para pintar esta parede, você vai precisar de {:.2f} litros de tinta.'.format(tinta))