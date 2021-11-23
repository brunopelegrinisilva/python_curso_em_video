#Exercicio 30 - Dizer se um numero eh par ou impar
num = int(input('Digite um numero inteiro: '))
if  num % 2 == 0:
    print('O numero digitado, {}, eh PAR!'.format(num))
else:
    print('O numero digitado, {}, eh IMPAR!'.format(num))