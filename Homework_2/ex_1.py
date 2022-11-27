# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:15:23 2021

@author: Ксения Камнева
"""

new_list = [1, 2.4, complex(1, 9), 'word', None, 9.456841]
# index = 0
# type_list = []
# while index < len(new_list):
#     type_list.append(type(new_list[index]))
#     print(f'Тип элемента {new_list[index]}: {type_list[index]})
#     index += 1

for element in new_list:
    print(f'Тип элемента {element}: {type(element)}')
    