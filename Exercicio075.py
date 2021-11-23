'''Ecercicio 075 Python Mundo 3, CeV Guanabara
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posicao foi digitado o primeiro valor 3
C) Quais foram os numeros pares'''
a = b = c = d = noves = pares = tres = 0
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))
tupla = (a, b, c, d)
for c in range(0, len(tupla)):
    if tupla[c] == 9:
        noves += 1
for d in range(0, len(tupla)):
    if tupla[d] % 2 == 0:
        pares += 1
print(f'A) O numero 9 foi digitado {noves} vezes.')
print(f'B) Em que posicao esta o primeiro numero 3? {tupla.index(3)+1}')
print(f'C) A quantidade de numeros pares digitadas foi {pares}.')
print(tupla)
