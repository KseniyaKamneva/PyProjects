# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:55:50 2022

@author: Ксения Камнева
"""

from random import randint

while True:
    try:
        num = int(input('Введите число: '))
        break
    except ValueError:
        print('Неверный формат данных!')
        
ran_list = [randint(-num,num) for _ in range(num)]
print(f'Массив:\n{ran_list}')

mult = 1

with open('file.txt', 'r') as file:
    nums = file.read().splitlines()

try:
    i = int(nums[0]) - 1
    j = int(nums[1]) - 1
except ValueError:
    print('Неверный формат данных в файле!')
    
mult = ran_list[i] * ran_list[j]
print(f'Произведение чисел на {i + 1} и {j + 1} позиции равно {mult}.')
