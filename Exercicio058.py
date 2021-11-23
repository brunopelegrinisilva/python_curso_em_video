'''Melhore o jogo do desafio 28, colocando tentativas ate 
acertar e a contagem de tentativas quando acertar, com dica de mais ou menos'''
from random import randint
jigsaw = randint(0, 10)
acertou = False
print('-=-'*20)
print("Vammos ver se consegue adivinhar meu numero, entre 0 e 10!")
print('-=-'*20)
tent = 0
while not acertou:
    tent += 1
    escolha = int(input("Digite o numero que voce escolheu : "))
    if escolha == jigsaw:
        acertou = True
    else:
        if jigsaw > escolha:
            print('Maior, mas errrrrrrou! Tente novamente!')
        else:
            print('Menor, mas errrrrrrou! Tente novamente!')
print('Acertou! Precisou de {} tentativas!'.format(tent))