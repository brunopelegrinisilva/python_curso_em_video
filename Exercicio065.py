'''Exercicio 065 Curso em Video Python Mundo 2
Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media
entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar se ele
quer continuar ou nao a digitar valores'''
soma = cont = maior = menor = n = 0
f = 'S'
while f in 'Ss':
    cont += 1
    n = int(input('Digite um numero: '))
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    f = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('Voce digitou: {} numeros e {} eh a soma deles, {} eh a media entre eles. O maior foi {} e o menor foi {}.'.format(cont,soma,(soma/cont), maior, menor))