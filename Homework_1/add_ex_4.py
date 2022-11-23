# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:41:19 2022

@author: Ксения Камнева
"""

while True:
    quarter = input('Введите номер четверти координатной плоскости: ')
    try:
        quarter = int(quarter)
        break
    except ValueError:
        print('Неверный формат данных!')
        
if quarter == 1:
    print('x > 0\ny > 0')
if quarter == 2:
    print('x < 0\ny > 0')
if quarter == 3:
    print('x < 0\ny < 0')
if quarter == 4:
    print('x > 0\ny < 0')
else:
    print('На координатной плоскости нет такой четверти')
