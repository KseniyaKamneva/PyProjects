# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:33:35 2023

@author: Ксения
"""

import chardet

words = ['разработка', 'администрирование', 'protocol', 'standart']
bytes_words = []

for word in words:
    word = word.encode('utf-8', errors='namereplace')
    bytes_words.append(word)
    print(word)

for word in bytes_words:
    print(word.decode(chardet.detect(word)['encoding']))
