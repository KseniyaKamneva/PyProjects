# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:05:44 2021

@author: Ксения Камнева
"""

from string import ascii_letters

def latin(new_str):
    if all(map(lambda letter: letter in ascii_letters, new_str)):
        return True
    else:
        return False

def int_func(new_str, only_first_word):
    if only_first_word == True:
        return new_str.capitalize()
    else:
        return new_str.title()

new_str = input('Введите строку в нижнем регистре: ')
if new_str.islower() and latin(new_str):
    print(int_func(new_str, True))
    print(int_func(new_str, False))
else:
    print('Некорректный ввод данных!')
