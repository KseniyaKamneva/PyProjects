# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:59:51 2023

@author: Ксения
"""

import binascii

words = [b'class', b'function', b'method']

for word in words:
    type_name = str(type(word)).replace("<class '", "Тип: ")
    print(type_name.replace("'>", ", слово:"), str(word).replace("b", ""), 
          binascii.hexlify(word), ", длина:", len(word))
