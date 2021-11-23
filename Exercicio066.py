'''Exercicio 066 Curso em Video Python 3 Mundo 2 Aula 15
Crie um programa que leia os numeros pelo teclado. O programa soh vai parar quando o usuario
digitar 999, mostrar quantos numeros digitados e a soma dele'''
n = s = c = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Q quantidade de numeros digitados foi {c} e a soma deles eh {s}')