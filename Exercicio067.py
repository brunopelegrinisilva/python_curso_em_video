'''Exercicio 067 Curso em Video Python 3 Mundo 2 Aula 15
Crie um programa que mostre a tabuada do numero digitado ate o usuario pedir a 
tabuada de um numero negativo'''
t = c = 0
print('-'*30)
print('-'*10, 'Tabuadas', '-'*10)
print('-'*30)
while True:
    t = int(input('Digite qual tabuada deseja: '))
    if t < 0:
        break
    print('-'*30)
    for c in range (1, 11):
        print(f'{t} x  {c} = {t * c}')    
    print('-'*30)
print('Done')