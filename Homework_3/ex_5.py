# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:05:38 2021

@author: Ксения Камнева
"""
def num_list(data, index):
    i = 0
    num_data = []
    while i < index:
        try:
            num_data.append(float(all_data[i]))
            i += 1
        except ValueError:
            i += 1
    return num_data
    
def num_sum(num_data):
    return sum(num_data)

special_symbol = '/'
data = []
while True:
    new_str = input('Введите числа, отделяя пробелами: ')
    all_data = new_str.split()
    try:
        data += num_list(all_data, all_data.index(special_symbol))
        print(num_sum(data))
        break
    except:
        data += num_list(all_data, len(all_data))
        print(num_sum(data))
