# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 00:21:42 2021

@author: Ксения Камнева
"""
def verification(arg):
    try:
        return float(arg)
    except ValueError:
        print('Неверный формат данных!')
        
def my_func(x, y, z):
    my_list = list((x, y, z))
    my_list.sort()
    my_sum = float(my_list[1]) + float(my_list[2])
    return my_sum

x, y, z = None, None, None

while x is None:
    x = verification(input('Введите первое число: '))
    
while y is None:
    y = verification(input('Введите второе число: '))
    
while z is None:
    z = verification(input('Введите третье число: '))

print(f'Сумма наибольших чисел равна {my_func(x, y, z)}')
