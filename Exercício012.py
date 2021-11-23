"""
Exercício 012 => Curso em vídeo
Feito dia 27/02/2020
"""
preco = float(input('Digite o Preço do Produto: R$ '))
desc = float(input('Quantos % de desconto concedido? '))
precofinal = preco * (1-(desc/100))
print('O preço digitado foi R$ {:.2f} e o desconto informado {:.2f} %, preço final é R$ {:.2f}'.format(preco, desc, precofinal))