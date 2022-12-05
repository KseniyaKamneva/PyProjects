# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 01:19:00 2021

@author: Ксения Камнева
"""
def my_func_1(x, y):
    return x ** y

def my_func_2(x, y):
    i = 0
    result = 1
    while i > y:
        result = result / x
        i -= 1
    return result

while True:
    try:
        x = float(input('Введите вещественное положительное число: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if x > 0:
        break
    print('Число не является положительным!')

while True:
    try:
        y = int(input('Введите целое отрицательное число: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if y < 0:
        break
    print('Число не является отрицательным!')

print(my_func_1(x, y))
print(my_func_2(x, y))
          