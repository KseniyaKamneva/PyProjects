# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 00:42:48 2021

@author: Ксения Камнева
"""

words = input('Введите строку из нескольких слов: ').split()
for index, element in enumerate(words, 1):  
    print(f'{index}: {element[:10]}')
