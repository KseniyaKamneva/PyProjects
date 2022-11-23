# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:58:30 2022

@author: Ксения Камнева
"""

while True:
    x1 = input('Введите X координату первой точки: ')
    y1 = input('Введите Y координату первой точки: ')
    x2 = input('Введите X координату второй точки: ')
    y2 = input('Введите Y координату второй точки: ')
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        break
    except ValueError:
        print('Неверный формат данных!')
        
dist = round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5), 3)
print(f'Расстояние между точками ({x1}, {y1}) и ({x2}, {y2}) равно {dist}')
