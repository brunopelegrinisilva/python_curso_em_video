'''Aula 016 Curso em Video Python Mundo 3 Aula 016 (primeira desse mundo)
TUPLAS
Tuplas sao imutaveis...'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}') # bom se precisar usar a posicao

#for comida in lanche:
#    print(f'Eu vou comer {comida}')    OS TRES JEITOS ESTAO CERTOS

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}.')
print('Comi pra caramba!')