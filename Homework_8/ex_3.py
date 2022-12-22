# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:41:50 2022

@author: Ксения
"""


class InvalidDivisorError(ZeroDivisionError):
    pass


def get_operand(name):
    while True:
        op = input(f"Введите {name.lower()}: ")
        abs_op = op[1:] if op.startswith("-") else op

        if abs_op.replace(".", "", 1).isdigit():
            break

        print(f"{name.title()} не является числом!")
    return float(op)


def divide(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        raise InvalidDivisorError("Делитель не может быть нулём!")


if __name__ == "__main__":
    dividend, divisor = get_operand("делимое"), get_operand("делитель")
    while True:
        try:
            print(divide(dividend, divisor))
        except InvalidDivisorError as exc:
            print(exc)
            divisor = get_operand("делитель")
        else:
            break
