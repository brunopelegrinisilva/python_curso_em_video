#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercício 021 => Curso em vídeo
Curso Python #08 - Utilizando Módulos
Feito dia  08/03/2020
"""
import pygame
pygame.init()
pygame.mixer.music.load('/home/brunopelegrini/Documentos/Python Studies/Curso_em_video/Ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
