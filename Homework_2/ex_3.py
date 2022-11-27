# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:54:52 2021

@author: Ксения Камнева
"""

seasons_list = ['зима', 'весна', 'лето', 'осень']
while True:
    try:
        month = int(input('Введите число из диапазона 1-12: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if month in range(1, 13):
        break
    print('Введено число не из диапазона 1-12!')
if month in range (9, 12):
    print(seasons_list[3])
elif month in range (6, 9):
    print(seasons_list[2])
elif month in range (3, 6):
    print(seasons_list[1])
else:
    print(seasons_list[0])
    