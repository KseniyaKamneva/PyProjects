# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 20:42:52 2022

@author: Ксения Камнева
"""

from functools import reduce

print(reduce(lambda a, b: a * b, [x for x in range(100,1001,2)]))
