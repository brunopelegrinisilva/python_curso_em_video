'''Exercicio 078 Mundo 3 Curso em Video CeV - Listas
Faca um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e suas respectivas posicoes na lista'''
lista = []
max = min = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite o primeiro numero para a posicao {cont}: ')))
    if cont == 0:
        max = min = lista[cont]
    else:
        if lista[cont] > max:
            max = lista[cont]
        if lista[cont] < min:
            min = lista[cont]
print('='*50)
print(f'Voce digitou os numeros {lista}')
# print(f'O maior numero digitado foi {max} e seu indice eh {lista.index(max)}.') Nao atende informar todas as posicoes do maior valor, desenvolvi sozinho
print(f'O maior numero digitado foi {max} e suas posicoes sao ', end="") # desenvolvi com suporte Guanabara
for i, v in enumerate(lista):
    if v == max:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min} e suas posicoes sao ', end='')
for i, v in enumerate(lista): #for utiliza indice na primeira e conteudo no segundo argumento, enumerate ainda preciso continuar exercitando para fixar
    if v == min:
        print(f'{i}...', end='')
print()
