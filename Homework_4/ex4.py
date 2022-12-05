# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:27:54 2022

@author: Ксения Камнева
"""

from random import randint

ran_list = [randint(-10,10) for _ in range(20)]
res_list = [el for el in ran_list if ran_list.count(el) == 1]
print(f'Исходный список:\n{ran_list}\nСписок без повторов:\n{res_list}')
