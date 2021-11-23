"""
Exercício 009 => Curso em vídeo
Feito dia 26/02/2020
Rate do dia 26/02/2020 USD para BRL: 4.4359
"""
reais = float(input('Quanto de dinheiro você tem na carteira? R$ '))
doletas = float(reais / 4.4359)
print('Com {:.2f} reais você consegue comprar {:.2f} dólares'.format(reais,doletas))