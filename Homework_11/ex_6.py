# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:48:45 2023

@author: Ксения
"""

import locale
from chardet import detect

def encoding():
    with open('test_file.txt', 'rb') as file:
        content = file.read()
    detected = detect(content)
    encoding = detected['encoding']
    text = content.decode(encoding)
    with open('test_file.txt', 'w', encoding='utf-8') as file:
        file.write(text)
            
print('Кодировка по умолчанию: ', locale.getpreferredencoding())
encoding()
with open('test_file.txt', encoding='utf-8') as file:
    content = file.read()
print(content)
