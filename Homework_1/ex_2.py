# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:36:48 2021

@author: Ксения Камнева
"""
while True:
    num_sec = input('Введите время в секундах: ')
    try:
        num_sec = int(num_sec)
    except ValueError: 
        print('Неверный формат данных!')
        continue
    if num_sec >= 0:
        break
    print('Вы ввели отрицательное число!')
        
hours = num_sec // 3600
minutes = (num_sec % 3600) // 60
seconds = num_sec % 60
print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
