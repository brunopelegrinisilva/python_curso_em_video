'''Exercicio 071 Curso em Video Python Aula 15
Crie um programa que simule um funcionamento de um caixa eletronico . No inicio, pergunte ao usuario
qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor
serao entregues. OBS:
considere que o caixa possui cedulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''
print('='*50)
print('{:^50}'.format('CAIXA ELETRONICO'))
print('='*50)
saque = int(input('Digite o valor a ser sacado: R$ '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*50)
print('Obrigado e volte sempre.')