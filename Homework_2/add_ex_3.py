# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:58:40 2022

@author: Ксения Камнева
"""

i = 0
sum_num = 0
num_list = []

while True:
    try:
        num = int(input('Введите число: '))
        break
    except ValueError:
        print('Неверный формат данных!')
        
while i < num:
    i += 1
    sum_num += round((1 + 1 / i) ** i)
    num_list.append(f'{i} : {sum_num}')
    
print(f'Набор сумм:\n{num_list}')
