# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
#  mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome eh {}'.format(nome[:(nome.find(' '))]))
print('Seu ultimo nome eh {}'.format(nome[(nome.rfind(' ')):]))
'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome eh {} '.format(nome[0]))
print('Seu ultimo nome eh {} '.format(nome[len(nome)-1]))