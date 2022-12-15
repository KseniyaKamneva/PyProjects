# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 01:33:03 2021

@author: Ксения Камнева
"""

from timeit import timeit
from memory_profiler import profile

@profile
def first():
    """ Сразу выполняется преобразование введенного значения к типу int,
    далее число проверяется на натуральность и производится сортировка.
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

@profile
def second():
    """Вводится число и проверяется на натуральность, преобразование к типу int
    производится при добавлении элемента в список. Сократилось время выполнения.
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


print(timeit("first()", setup = "from __main__ import first", number = 1))
print(timeit("second()", setup = "from __main__ import second", number = 1))
