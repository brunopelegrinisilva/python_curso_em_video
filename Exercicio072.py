'''Exercicio 72 Mundo 3 Python CeV Guanabara, TUPLAS
Ler um numero para extenso, de 0 a 20.'''
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
while True:    
    while True:
        num = int(input('Digite um numero de 0 a 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Tente novamente.')
    print(f'Voce digitou o numero {cont[num]}.')
    end = str(input('Voce quer continuar?: ')).upper().strip()[0]
    if end == "N":
        break