# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:23:11 2022

@author: Ксения Камнева
"""

from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time*rate + bonus}")
    except ValueError:
        print("Некорректный ввод! Введите 3 числа.")
        
salary()
