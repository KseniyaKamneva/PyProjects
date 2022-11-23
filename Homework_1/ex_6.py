# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:30:09 2021

@author: Ксения Камнева
"""
while True:
    a = input('Введите результат первого дня: ')
    b = input('Введите итоговый результат: ')
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print('Неверный формат данных!')
        continue
    if a > 0 and b > a:
        break
    print('Введены некорректные значения.')

day = 1    
while a < b:
    a = 1.1 * a
    day = day + 1
print('\nСпортсмен достиг результата', b,'км на', day,'день.')
