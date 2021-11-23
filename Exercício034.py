# Exercício Python 034: Escreva um programa que pergunte o salário 
# de um funcionário e calcule o valor do seu aumento. Para salários superiores 
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salario atual: R$ '))
novosalario = 0
if salario > 1250:
    novosalario = salario * 1.1
else:
    novosalario = salario * 1.15
print('O novo salario do funcionario sera de RS {:.2f}'.format(novosalario))
    