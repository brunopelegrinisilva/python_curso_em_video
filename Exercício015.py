"""
Exercício 014 => Curso em vídeo
Feito dia 27/02/2020
"""
dias = int(input('Digite por quantos dias o carro foi alugado: '))
km = int(input('Digite quantos Km percorreu nesse período: '))
print('O custo total da locação foi de R$ {:.2f}'.format((dias*60+km*0.15)))
