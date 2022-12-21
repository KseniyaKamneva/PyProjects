# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:55:04 2022

@author: Ксения Камнева
"""


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity
        
    def __add__(self, other):
        return self.quantity + other.quantity
    
    def __sub__(self, other):
        return self.quantity - other.quantity
        
    def __mul__(self, other):
        return self.quantity * other.quantity
        
    def __truediv__(self, other):
       return self.quantity // other.quantity 
        
    def make_order(self, rows):
        cells_per_row = self.quantity // rows
        result = ["*" * rows for _ in range(cells_per_row)]
        
        remainder = self.quantity % rows
        if remainder:
            result.append("*" * remainder)
    
        return "\n".join(result)


if __name__ == "__main__":
    quantity = int(input("Введите количество клеток: "))
    cell = Cell(quantity)
    
    rows = int(input("Введите количество рядов: "))
    print(cell.make_order(rows))
