#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercício 018 => Curso em vídeo
Curso Python #08 - Utilizando Módulos
Feito dia  08/03/2020
"""
import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O nome escolhido foi {}'.format(escolhido))



