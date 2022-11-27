# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 00:28:27 2021

@author: Ксения Камнева
"""
seasons_dict = dict(winter='зима', spring='весна', summer='лето', autumn='осень')
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
    print(seasons_dict.get('autumn'))
elif month in range (6, 9):
    print(seasons_dict.get('summer'))
elif month in range (3, 6):
    print(seasons_dict.get('spring'))
else:
    print(seasons_dict.get('winter'))
    