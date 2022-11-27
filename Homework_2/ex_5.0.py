# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 01:33:03 2021

@author: Ксения Камнева
"""

rating = [7, 6, 4, 2, 15, 8]
while True:
    try:
        element = int(input('Введите натуральное число: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if element > 0:
        rating.append(element)
        rating.sort(reverse=True)
        break
    print('Это ненатуральное число!')
print(rating)
