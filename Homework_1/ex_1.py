# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:16:48 2021

@author: Ксения Камнева
"""
while True:
    first_var = input('Введите значение первой переменной: ')
    second_var = input('Введите значение второй переменной: ')
    try:
        first_var = float(first_var)
        second_var = float(second_var)
        break
    except ValueError:
        print('Неверный формат данных!')

res_sum = first_var + second_var
res_dif = first_var - second_var
res_mult = first_var * second_var
print(f'\nПервая переменная: {first_var}\nВторая переменная: {second_var}\nСумма равна {res_sum:.3f}\nРазность равна {res_dif:.3f}.\nПроизведение равно {res_mult:.3f}')
if second_var == 0:
    res_div = print('Делить на нуль нельзя!')
else:
    res_div = first_var / second_var
    print(f'Частное равно {res_div:.3f}')

str_var = input('Введите строку:')
print(str_var)
