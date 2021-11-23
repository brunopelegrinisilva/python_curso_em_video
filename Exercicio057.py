'''Exercicio 57 Curso em video aula 14 Estrutura de Repeticao While'''
sexo = str(input('Informe seu Sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))