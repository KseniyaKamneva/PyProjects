# -*- coding: utf-8 -*-
"""
Created on Thu May 26 01:10:52 2022

@author: Ксения Камнева
"""

import time
import itertools

class TrafficLight:
    _color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]
    
    def running(self):
        for light in itertools.cycle(self._color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end ="")
            time.sleep(light[1][0])
            
trf = TrafficLight()
trf.running()
