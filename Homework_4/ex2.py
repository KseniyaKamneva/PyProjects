# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:35:40 2022

@author: Ксения Камнева
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num-1]]
print(res_list)
