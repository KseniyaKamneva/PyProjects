# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:56:54 2022

@author: Ксения Камнева
"""

while True:
    n = input('Введите день недели: ')
    try:
        n = int(n)
    except ValueError:
        print('Неверный формат данных!')
        continue
    if 0 < n < 8:
        break
    print('В неделе только 7 дней.')
    
if 0 < n <= 5:
    print('Это будний день.')
else:
    print('Это выходной день.')
