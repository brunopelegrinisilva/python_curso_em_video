#Exercicio 29 - Medir velocidade atual e multar se acima de 80km/h em R$ 20/km excedido
v = float(input('Digite a velocidade atual do carro: '))
if v > 80:
    m = (v-80)*7
    print('MULTADO! Voce ultrapassou o limite precedido que eh de 80km/h!')
    print('Voce deve pagar uma multa de R$ {:.2f} '.format(m))
print('Tenha um bom dia! Dirija com seguranca!')