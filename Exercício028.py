#Exercicio 28 - Adivinhacao entre 0 e 5
from random import randint
from time import sleep
print('-=-'*20)
print("I wanna play a game, chose a number between 0 and 5...")
print('-=-'*20)
escolha = int(input("Digite o numero que voce escolheu : "))
jigsaw = randint(0, 5)
print('Processando...')
sleep(3)
if escolha == jigsaw:
    print("Voce acertou, parabens voce venceu!")
else:
    print("Voce perdeu, hahahahaha!!! Eu escolhi {} e voce {}!".format(jigsaw, escolha))