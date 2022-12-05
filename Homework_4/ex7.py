# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:06:11 2022

@author: Ксения Камнева
"""

def factorial(num):
    f_num = 1
    if num == 0:
        yield f'{num}! = 1'
    for i in range(1, num + 1):
        f_num *= i
        yield f'{i}! = {f_num}'

for el in factorial(int(input('Факториал числа: '))):
    print(el)
