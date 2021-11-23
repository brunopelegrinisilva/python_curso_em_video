'''Exercicio 069 Aula 15 Curso em Video Python Mundo 2
Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa
devera perguntar se o usuario quer ou nao continuar. No final, mostre:
a - quantas pessoas maiores de 18 anos
b - quantos homens foram cadastrados
c - quantas mulheres tem menos de 20 anos'''
print('='*50)
print('='*20, 'CADASTRO','='*20)
print('='*50)
tm = idade = m20 = p18 = 0
gen = fim = ' '
while True:
    while gen not in "MF":
        gen = str(input('Qual sexo da pessoa a ser cadastrada? [M/F]: ')).upper().strip()[0]
    print('='*50)
    if gen == 'M':
        tm += 1
    idade = int(input('Digite a idade da pessoa cadastrada: '))
    print('='*50)
    if idade >= 18:
        p18 += 1
    if gen == 'F' and idade < 20:
        m20 += 1
    while fim not in 'SN':
        fim = str(input('Quer adicionar mais um cadastro? [S/N]: ')).upper().strip()[0]
    print('='*50)
    if fim == 'N':
        break
print('Estatistica solicitada:')
print(f'Total de cadastrados maiores de 18 anos: {p18}.')
print(f'Total de homens cadastrados: {tm}.')
print(f'Total de mulheres cadastradas com menos de 20 anos: {m20}.')