# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:58:55 2021

@author: Ксения Камнева
"""

while True:
    n = input('Введите число: ')
    try:
        n = int(n)
    except ValueError:
        print('Неверный формат данных!')
        continue
    if n >= 0:
        break
    print('Введено отрицательное число!')

if n < 10:
    max_n = n
else:
    max_n = 0
    while n > 10:
        current_n = n % 10
        n = n // 10
        if current_n > max_n:
            max_n = current_n
print(max_n)
