# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 20:46:03 2022

@author: Ксения Камнева
"""

from itertools import count, cycle

print('Программа генерирует целые числа. Для генерации следующего нажмите "Enter", для выхода - "q"')
for i in count(int(input('Введите начальное число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы списка. Для продолжения нажмите "Enter", для выхода - "q"')
new_list = input('Введите список через пробел: ').split()
iter_ = cycle(new_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()
    