# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 20:27:22 2022

@author: Ксения Камнева
"""

from functools import reduce

def mult_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"Список: \n{uniq_list}\nПроизведение элементов списка:\n{reduce(mult_list, uniq_list)}")
