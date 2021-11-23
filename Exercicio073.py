'''Exercicio 73 Mundo 3 Python, Tuplas, CeV Guanabara
Criar uma Tupla com os 20 primeiros colocados do campeonato brasileiro na ordem de colocacao. Depois mostre:
a) os 5 primeiros times;
b) os ultimos 4 colocados;
c) os times em ordem alfabetica;
d) em que posicao esta o time da Chapecoense.'''
camp = ('Atletico-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atletico-GO', 'Atletico-PR'
        , 'Ceara-SC', 'Cuiaba', 'Internacional', 'Fluminense', 'Santos', 'Juventude', 'Sao Paulo', 'Bahia', 'America-MG',
        'Sport Recife', 'Gremio', 'Chapecoense')
prim = num = 0
ult = 19
print('='*50)
print('{:^50}'.format('CAMPEONATO BRASILEIRO 2021'))
print('='*50)
print(f'Lista de times: {camp}')
print('='*50)
while True:
    print('''1 - Os 5 primeiros colocados
2 - A zona de Rebaixamento
3 - Lista de times em ordem alfabetica
4 - A posicao do Chapecoense
5 - Sair do Programa''')
    num = int(input('Digite a opcao desejada: '))
    if 0 < num > 4:
        break
    elif num == 1:
        print('Os 5 primeiros colocados sao:')
        while prim < 5:
            print(camp[prim])
            prim += 1
    elif num == 2:
        print('A zona de rebaixamento tem os times:')
        while ult > 15:
            print(camp[ult])
            ult -= 1
    elif num == 3:
        print(sorted(camp))
    elif num == 4:
        print('O Chapecoense esta na na {}a posicao no momento.'.format(camp.index('Chapecoense')+1))
    print('='*50)
print('Obrigado por usar nosso programa.')
        