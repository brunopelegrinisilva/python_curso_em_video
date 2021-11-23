"""
Exercício 008 => Curso em vídeo
Feito dia 26/02/2020
Nota sobre as conversões: base metro
km = 1000 - Kilometro
hm = 100 - Hectômetro
dam = 10 - Decametro
m =  1 - Metro
dm = 0,1 - Decímetro
cm = 0,01 - Centímetro
mm = 0,001 - milímetro
"""
m = float(input('Digite uma distância em metros: '))
print('A distância inserida equivale à {} kilômetros'.format(m/1000))
print('A distância inserida equivale à {} hectômetros'.format(m/100))
print('A distância inserida equivale à {} decametros'.format(m/10))
print('A distância inserida equivale à {:.0f} metros'.format(m))
print('A distância inserida equivale à {:.0f} decímetros'.format(m/0.1))
print('A distância inserida equivale à {:.0f} centímetros'.format(m/0.01))
print('A distância inserida equivale à {:.0f} milímetros'.format(m/0.001))