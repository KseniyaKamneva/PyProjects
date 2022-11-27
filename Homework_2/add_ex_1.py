# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:22:16 2022

@author: Ксения Камнева
"""

i = 0
sum_num = 0

while True:
    string = input('Введите вещественное число: ')
    try:
        num = float(string)
        break
    except ValueError:
        print('Неверный формат данных!')
        
while i < len(string):
    try:
        sum_num += int(string[i])
        i += 1
    except ValueError:
        i += 1
        continue
    
print(f'Сумма цифр числа {string} равна {sum_num}.')
