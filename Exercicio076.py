'''Exercicio 076 Mundo 3 Python, CeV Guanabara
Crie um programa que tenha uma tupla unica com nome de produto e preco, respectivamente,
em sequencia. No final, mostre uma listagem de precis, organizando os dados em forma tabular'''
listagem = (str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: ')),
            str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: ')),
            str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: ')),
            str(input('Digite o nome do produto: ')), float(input('Digite o preco do produto: ')),)
print('='*40)
print(f'{"Listagem de Precos":^40}')
print('='*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
