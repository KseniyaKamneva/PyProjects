# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:41:50 2022

@author: Ксения
"""

class ExceptDivision:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def division(dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return ('Делить на нуль нельзя!')


dividend = float(input('Введите делимое: '))
divisor = float(input('Введите делитель: '))
print(ExceptDivision.division(dividend, divisor))
