# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:55:04 2022

@author: Ксения Камнева
"""


class Cell:
    def __init__(self, quantity):
        self.quantity = abs(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        return self.quantity - other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __repr__(self):
        return f"{self.quantity} ячеек"

    def make_order(self, cells_per_row):
        rows_num = self.quantity // cells_per_row
        result = ["*" * cells_per_row for _ in range(rows_num)]

        remainder = self.quantity % cells_per_row
        if remainder > 0:
            result.append("*" * remainder)

        return "\n".join(result)


if __name__ == "__main__":
    print("Создаём объекты клеток...")
    cell1 = Cell(30)
    cell2 = Cell(25)
    cell3 = Cell(10)
    cell4 = Cell(15)
    print("Готово!")

    print()
    print("Складываем клетки...")
    print(
        f"В первой клетке {cell1}, во второй клетке {cell2},",
        f"результат: {cell1 + cell2}",
    )

    print()
    print("Вычитаем клетки...")
    cells = (cell1, cell2, cell3, cell4)
    for i in range(len(cells)):
        c1, c2 = cells[i - 2], cells[i - 1]
        print(f"В первой клетке {c1}, во второй клетке {c2},", end=" ")
        if c1.quantity >= c2.quantity:
            print("результат:", c1 - c2)
        else:
            print(
                "поэтому невозможно выполнить операцию",
                "(результат вычитания не может быть отрицательным)",
            )

    print()
    print("Перемножаем клетки...")
    print(
        f"В первой клетке {cell2}, во второй клетке {cell3},",
        f"результат: {cell2 * cell3}",
    )

    print()
    print("Делим клетки...")
    print(
        f"В первой клетке {cell1}, во второй клетке {cell4},",
        f"результат: {cell1 / cell4}",
    )

    print()
    print("Организация ячеек по рядам...")
    cells_per_row = 5
    print(f"Разбиваем клетку из {cell1} на ряды по {cells_per_row} ячеек:")
    print(cell1.make_order(cells_per_row))
    cells_per_row = 10
    print(f"Разбиваем клетку из {cell2} на ряды по {cells_per_row} ячеек:")
    print(cell2.make_order(cells_per_row))
