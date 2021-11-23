'''
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas;
– Quantas letras ao todo (sem considerar espaços);
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip() #.strip() remove espacos antes e depois
print('Analisando seu nome...')
print('Seu nome em maiusculas eh : {}' .format(nome.upper()))
print('Seu nome em minusculas eh : {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras, sem considerar os espacos'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) 