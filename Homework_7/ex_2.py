# -*- coding: utf-8 -*-
"""
Created on Thu May 26 01:25:06 2022

@author: Ксения Камнева
"""

class Road:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def get_full_proft(self):
        return f"{self._length} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"
    
road_1 = Road(5000, 20)
print(road_1.get_full_proft())
          