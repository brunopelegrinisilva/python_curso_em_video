#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercício 020 => Curso em vídeo
Curso Python #08 - Utilizando Módulos
Feito dia  08/03/2020
"""
from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceito aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentacao e:')
print(lista)