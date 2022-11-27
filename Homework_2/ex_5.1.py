# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 02:10:41 2021

@author: Ксения Камнева
"""

rating = [7, 6, 4, 2, 15, 8]
while True:
    element = input('Введите натуральное число: ')
    if element.isdecimal() and element != '0':
        rating.append(int(element))
        rating.sort(reverse=True)
        break
    print('Неверный формат данных!')
print(rating)
