# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 22:14:36 2021

@author: Ксения Камнева
"""
    
def verification(arg):
    try:
        return float(arg)
    except ValueError:
        print('Неверный формат данных!')

def division(x, y):
    return x / y

x, y = None, None

while x is None:
    x = verification(input('Введите делимое: '))
        
while not y:
    y = verification(input('Введите делитель: '))
    if y == 0:
        print('На нуль делить нельзя!')

print(f'{x}/{y} = {division(x, y)}')
