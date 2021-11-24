'''Exercicio 079 Mundo 3 Python CeV
Crie um programa onde o usuario pode digitar varios valores numericos e cadastre-os em uma lista.
Caso o numero ja exista, nao sera adicionado. No final, serao exibidos todos os valores unicos digitados
em oderm crescente.'''
lista = []
while True:
    c = int(input(f'Insira um numero na lista: '))
    if c not in lista:
        lista.append(c)
    else:
        print('Numero ja adicionado, favor escolher outro.')
    end = str(input(f'Voce quer continuar? (S/N) ')).upper().strip()[0]
    if end == 'N':
        break
lista.sort()
print(f'A lista digitada, em ordem, foi: {lista}')
