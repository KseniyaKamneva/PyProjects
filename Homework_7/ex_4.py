# -*- coding: utf-8 -*-
"""
Created on Thu May 26 01:46:47 2022

@author: Ксения Камнева
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self.__color = color
        self.__name = name
        self.__is_police = is_police

    def go(self):
        print(f'{self.__color} {self.__name} is running!')

    def stop(self):
        print(f'{self.__color} {self.__name} stopped')

    def turn_direction(self, direction):
        print(f'{self.__color} {self.__name} turned {direction}')

    def show_speed(self):
        print(f'Current car speed = {self._speed}')

    def is_police_car(self):
        return self.__is_police


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print("Over speed for town car!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print("Over speed for work car!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


def operations_with_car(car):
    car.go()
    car.turn_direction("Left")
    car.turn_direction("Right")
    car.show_speed()
    print("The car is police: ", car.is_police_car())
    car.stop()

# Town car
# speed = int(input("Input speed for town car: "))
# color = input("Input color for town car: ")
# name = input("Input name for town car: ")
speed = 65
color = 'Red'
name = 'TownCar'
town_car = TownCar(speed, color, name)
operations_with_car(town_car)
# Work car
# speed = int(input("Input speed for work car: "))
# color = input("Input color for work car: ")
# name = input("Input name for work car: ")
speed = 45
color = 'Yellow'
name = 'WorkCar'
work_car = WorkCar(speed, color, name)
operations_with_car(work_car)
# Police car
# speed = int(input("Input speed for police car: "))
# color = input("Input color for police car: ")
# name = input("Input name for police car: ")
speed = 120
color = 'Blue'
name = 'PoliceCar'
police_car = PoliceCar(speed, color, name)
operations_with_car(police_car)
