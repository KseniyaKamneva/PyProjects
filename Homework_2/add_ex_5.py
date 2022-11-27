# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:31:22 2022

@author: Ксения Камнева
"""

def add_list(data, index):
    i = 0
    data_list = []
    while i < index:
        try:
            data_list.append(all_data[i])
            i += 1
        except ValueError:
            i += 1
    return data_list

import random

data = []
new_str = input('Введите данные, отделяя пробелами: ')
all_data = new_str.split()
data = add_list(all_data, len(all_data))
print(f'Исходный список: {data}')
random.shuffle(data)
print(f'Перемешанный список: {data}.')
      