"""
Created on Mon May 23 01:20:44 2022

@author: Ксения Камнева
"""

with open('1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите новую строку: ')
        if not line:
            break
        f.write(f'{line}\n')
