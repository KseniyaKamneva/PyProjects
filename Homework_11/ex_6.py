# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:48:45 2023

@author: Ксения
"""

import locale

print('Кодировка по умолчанию: ', locale.getpreferredencoding())

with open('test_file.txt', encoding='utf-8', errors='replace') as file:
    print(file.read())
