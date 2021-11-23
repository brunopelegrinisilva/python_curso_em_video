'''Ecercicio 075 Python Mundo 3, CeV Guanabara
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posicao foi digitado o primeiro valor 3
C) Quais foram os numeros pares'''
tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))
         , int(input('Digite um valor: ')))
print(f'Voce digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posicao.')
else:
    print('Nao foi digitado nenhum numero 3.')
print('Os numeros pares digitados foram: ', end = '')
for x in tupla:
    if x % 2 == 0:
        print(x, end=' ')