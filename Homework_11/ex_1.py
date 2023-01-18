# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:26:05 2023

@author: Ксения
"""

words = ['разработка', 'сокет', 'декоратор']

for word in words:
    type_name = str(type(word)).replace("<class '", "Тип: ")
    print(type_name.replace("'>", ", слово:"), word)

uni_words = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
'\u0441\u043e\u043a\u0435\u0442','\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for word in uni_words:
    type_name = str(type(word)).replace("<class '", "Тип: ")
    print(type_name.replace("'>", ", слово:"), word)
