'''Exercicio 082 Mundo 3 Python'''
lista = []
listap = []
listai = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'A lista completa eh: {lista}.')
print(f'A lista dos pares eh: {listap}.')
print(f'A lista dos impares eh: {listai}.')
