# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:12:16 2022

@author: Ксения Камнева
"""

x = input('Введите X: ')
y = input('Введите Y: ')
z = input('Введите Z: ')

left_exp = not(x or y or z)
right_exp = not x and not y and not z
print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} ?', left_exp is right_exp)
