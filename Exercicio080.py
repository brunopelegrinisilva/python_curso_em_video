'''Exercicio 080 Mundo 3 Python Curso em Video - Exercício Python 080: Crie um programa onde o usuário 
possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista.')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados foram {lista}') #assisti do Guanabara, hint to self, nao esqueca de usar [] com listas.