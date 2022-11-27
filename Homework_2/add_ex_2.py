# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:43:58 2022

@author: Ксения Камнева
"""

i = 0
mult = 1
num_list = []

while True:
    try:
        num = int(input('Введите число: '))
        break
    except ValueError:
        print('Неверный формат данных!')
        
while i < num:
    num_list.append(mult)
    i += 1
    mult *= i + 1
    
print(f'Набор произведений:\n{num_list}')
