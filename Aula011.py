# Aula 11 - Cores no terminal, padrao ANSI
print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')

print('\033[0;32;41mTeste\033[m')

a = 'Teste'

print('{}{}{}'.format('\033[1;32;41m', a, '\033[m'))