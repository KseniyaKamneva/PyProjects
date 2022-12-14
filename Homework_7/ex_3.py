# -*- coding: utf-8 -*-
"""
Created on Thu May 26 01:34:40 2022

@author: Ксения Камнева
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}
        
class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_full_profit(self):
        return f"{sum(self._income.values())}"
    
manager = Position("Ivan", "Ivanov", "Boss", 500000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())
    