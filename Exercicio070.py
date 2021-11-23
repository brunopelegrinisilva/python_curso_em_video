'''Exercicio 070 Curso em Video Python Mundo 2 Aula 15
Crie um programa que leia o nome de varios produtos. O programa devera pergutar se o usuario quer
continuar ou nao. No final, mostre:
a - total gasto na compra
b - quantos produtos custam mais de R$ 1000,00
c - qual o nome do produto mais barato'''
print('='*49)
print('='*20,'COMPRAS','='*20)
print('='*49)
produto = barato = ' '
preco = mais1k = total = menor = 0
while True:
    fim = ' '
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: R$ '))
    total += preco
    if preco > 1000:
        mais1k += 1
    if total == preco or menor > preco:
        barato = produto
        menor = preco
    print('='*49)
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if fim == 'N':
        break
print('='*49)
print(f'Total em compras: R$ {total:.2f}')
print(f'Quantidade de produtos acima de R$ 1.000,00: {mais1k}.')
print(f'O produto mais barato foi o {barato}, custando R$ {menor:.2f}.')
