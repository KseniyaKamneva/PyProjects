# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 01:05:56 2021

@author: Ксения
"""
seasons = dict(зима=(1,2,12), весна=(3,4,5), лето=(6,7,8), осень=(9,10,11))
while True:
    try:
        month = int(input('Введите число из диапазона 1-12: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if month in range(1, 13):
        break
    print('Введено число не из диапазона 1-12!')
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
        break
