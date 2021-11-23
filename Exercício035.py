# Exercício Python 035: Desenvolva um programa que leia o 
# comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('Sim, eh possivel formar um triangulo')
else:
    print('Nao, nao eh possivel formar um triangulo')
