# -*- coding: utf-8 -*-
"""
Created on Thu May 26 02:31:15 2022

@author: Ксения Камнева
"""

class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print(f'{self._title}: Start drawing in parent class')


class Pen(Stationery):
    def draw(self):
        print(f'{self._title}: Start drawing child class Pen')


class Pencil(Stationery):
    def draw(self):
        print(f'{self._title}: Start drawing child class Pencil')


class Handle(Stationery):
    def draw(self):
        print(f'{self._title}: Start drawing child class Handle')


stationery = Stationery("Parent title")
stationery.draw()

pen = Pen("Pen Title")
pen.draw()

pencil = Pencil("Pencil Title")
pencil.draw()

handle = Handle("Handle Title")
handle.draw()
