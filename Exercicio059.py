'''Exercio 059 Curso em Video, crie um programa que leia dois valores e mostre
um menu como ao lado da tela, sendo opcao 1 somar, 2 multiplicar, 3 maior , 4 novos numeros e 5 sair
do programa.'''
from time import sleep
print('='*100)
escolha = 0
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
while escolha != 5:
    print('='*100)
    print('Escolha o que deseja fazer com os numeros digitados, conforme abaixo.')
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos Numeros')
    print('[5] - Sair do Programa')
    escolha = int(input('Digite opcao escolhida: '))
    if escolha == 1:
        print('A soma dos numeros digitados eh {}.'.format(num1+num2))
    elif escolha == 2:
        print('A multiplicacao dos numeros digitados eh {}.'.format(num1*num2))
    elif escolha == 3:
        print('O maior dos numeros digitados eh o {}'.format(max(num1,num2)))
    elif escolha == 4:
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))      
    sleep(1)
print('='*100)
print('Programa encerrado conforme solicitado, obrigado!')
print('='*100)
