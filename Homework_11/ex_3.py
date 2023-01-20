# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:20:53 2023

@author: Ксения
"""

words = ["b'attribute'", "b'класс'", "b'функция'", "b'type'"]

for word in words:
    try:
        word = eval(word)
    except:
        print(word.replace('b', ''), 'нельзя перевести в байтовый тип.')  
  