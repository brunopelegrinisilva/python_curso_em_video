"""
Exercício 013 => Curso em vídeo
Feito dia 27/02/2020
"""
salario = float(input('Digite o Salário atual: R$ '))
aumento = float(input('Quantos % de aumento concedido? '))
salfinal = salario * (1+(aumento/100))
print('O salário digitado foi R$ {:.2f} e o aumento informado {:.2f} %, salário final é R$ {:.2f}'.format(salario, aumento, precofinal))
