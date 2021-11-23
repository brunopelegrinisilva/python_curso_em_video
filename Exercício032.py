#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime
ano = int(input('Digite um ano para saber se ele eh bissexto. Para usar o ano atual, digite 0: '))
if ano == 0:
    ano = datetime.date.today().year
if ano%4==0 and ano%100!=0:
    print('Sim, o ano {} que foi digitado eh BISSEXTO'.format(ano))
elif ano%400==0:
    print('Sim, o ano {} que foi digitado eh BISSEXTO'.format(ano))
else:
    print('Nao, o ano {} que foi digitado NAO eh BISSEXTO'.format(ano))
