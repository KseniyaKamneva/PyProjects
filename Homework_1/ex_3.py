# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:27:28 2021

@author: Ксения Камнева
"""
while True:
    n = input('Введите число n: ')
    m = len(n)
    try:
        n = int(n)
        break
    except ValueError:
        print('Неверный формат данных!')
       
if n < 0:
    m = m - 1
else:
    m = m

#Вариант 1 (с разбиением на переменные и выводом выражения)

double_n = n * (10**m + 1)
triple_n = n * (10**(2*m)) + double_n
result = sum((triple_n, double_n, n))
print(f'{triple_n} + {double_n} + {n} =', result)

#Вариант 2 (без разбиения на переменные и выводом результата)

# result = n * ( 10**(2*m) + 2 * 10**m + 3)
# print(result)
