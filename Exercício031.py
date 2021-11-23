# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
#  parta viagens mais longas.

d = float(input('Qual eh a distancia da sua viagem em km? '))
print('Voce esta prestes a comecar uma viagem de {:.1f} quilometros'.format(d))
if d>=200:
    print('E o preco de sua passagem sera de R$ {:.2f}.'.format(d*0.45))
else:
    print('E o preco de sua passagem sera de R$ {:.2f}.'.format(d*0.5))