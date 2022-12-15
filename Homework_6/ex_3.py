# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:54:52 2021

@author: Ксения Камнева
"""
from timeit import timeit
from memory_profiler import profile
from sys import getsizeof
from pympler.asizeof import asizeof

@profile
def first():
    """Задается список и сопоставление ведется по индексу элемента. Самый долгий.
    Самый меньший расход памяти.
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
    print(getsizeof(seasons_list))
    print(asizeof(seasons_list))  


@profile
def second():
    """Задается словарь и сопоставление ведется по значениям, результатом будет 
    ключ. Один из самых быстрых.
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
    print(getsizeof(seasons))
    print(asizeof(seasons))
    
    
@profile
def third():
    """Задается словарь и сопоставление ведется по ключам, результатом будет значение.
    Используется метод dict.get()
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
    print(getsizeof(seasons_dict))
    print(asizeof(seasons_dict))

@profile
def fourth():
    """Задается словарь и сопоставление ведется по значениям, результатом будет ключ.
    Используется метод dict.keys(). Один из самых быстрых."""
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
    print(getsizeof(seasons))
    print(asizeof(seasons))

print(timeit("first()", setup = "from __main__ import first", number = 1))
print(timeit("second()", setup = "from __main__ import second", number = 1))
print(timeit("third()", setup = "from __main__ import third", number = 1))
print(timeit("fourth()", setup = "from __main__ import fourth", number = 1))
