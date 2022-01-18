'''Exercicio 81 Mundo 3 Python'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('='*30)
print(f'Voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente sao: {lista}.')
if 5 in lista:
    print('O numero 5 esta na lista!')
else:
    print('O numero 5 nao esta na lista!')
    