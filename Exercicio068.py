'''Exercicio 068 Curso em Video Python 3 Mundo 2 Aula 15
Crie um programa que jogue par ou impar com o usuario e continue ate que o usuario
perca, mostrando a quantidade de vezes que ganhou'''
from random import randint
from time import sleep
print('='*42)
print('='*10,'JOGANDO PAR OU IMPAR','='*10)
print('='*42)
p1n = p2n = res = v1 = 0
while True:
    p1n = int(input('Escolha seu numero: '))
    p1o = str(input('Voce quer Par ou Impar [P/I] ?: ')).upper().strip()[0]
    p2n = randint(0,10)
    res = p1n + p2n
    sleep(1)
    print(f'Voce jogou {p1n} e o computador {p2n}, no total deu {res}.')
    print(f'DEU PAR!' if res % 2 == 0 else 'DEU IMPAR!')
    if res % 2 == 0:
        if p1o == 'P':
            v1 += 1
            print('Voce venceu! Jogue novamente.')
        else:
            break
    else:
        if p1o == 'I':
            v1 += 1
            print('Voce venceu! Jogue novamente.')
        else:
            break
print('='*42)
print('Voce perdeu!')
print(f'Voce venceu um total de {v1} vezes.')
