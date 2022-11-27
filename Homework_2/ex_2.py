# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:17:44 2021

@author: Ксения Камнева
"""

new_str = input('Введите список элементов через запятую: ')
new_list = new_str.split(',')
print(new_list)
# index = 1
# while index < len(new_list):
#     new_list[index], new_list[index-1] = new_list[index-1], new_list[index]
#     index += 2

length = len(new_list)
for index in range(1, length, 2):
    new_list[index], new_list[index-1] = new_list[index-1], new_list[index]
print(new_list)
