'''Exercicio 73 Mundo 3 Python, Tuplas, CeV Guanabara
Criar uma Tupla com os 20 primeiros colocados do campeonato brasileiro na ordem de colocacao. Depois mostre:
a) os 5 primeiros times;
b) os ultimos 4 colocados;
c) os times em ordem alfabetica;
d) em que posicao esta o time da Chapecoense.'''
camp = ('Atletico-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atletico-GO', 'Atletico-PR'
        , 'Ceara-SC', 'Cuiaba', 'Internacional', 'Fluminense', 'Santos', 'Juventude', 'Sao Paulo', 'Bahia', 'America-MG',
        'Sport Recife', 'Gremio', 'Chapecoense')
print('='*50)
print('{:^50}'.format('CAMPEONATO BRASILEIRO 2021'))
print('='*50)
print(f'Lista de times: {camp}')
print('='*50)
print(f'Os 5 primeiros sao: {camp[0:4]}')
print('='*50)
print(f'Os 4 ultimos colocados sao: {camp[-4:]}')
print('='*50)
print(f'A lista de times em ordem alfabetica: {sorted(camp)}')
print('='*50)
print(f'O Chapecoense esta na {camp.index("Chapecoense")+1}a posicao')