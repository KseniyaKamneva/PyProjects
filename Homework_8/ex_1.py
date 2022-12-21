"""
Created on Mon May 30 12:24:13 2022

@author: Ксения Камнева
"""


class Matrix:
    def __init__(self, data):
        self.data = data
        self._rows_count = len(data)
        self._cols_count = len(data[0]) if self._rows_count else 0
        self._index = -1

    @property
    def dimensions(self):
        return self._rows_count, self._cols_count

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index < self._rows_count:
            return self.data[self._index]
        raise StopIteration()

    def __add__(self, other: "Matrix"):
        result_matrix = []
        # Сопоставляем матрицы по строкам и упаковываем строки в кортежи.
        collated_data = zip(self.data, other.data)
        for zrows in collated_data:
            zcols = zip(*zrows)  # Сопоставляем строки по столбцам.
            result_row = list(map(sum, zcols))
            result_matrix.append(result_row)
        return Matrix(result_matrix)


def fill_matrix(rows, columns):
    data = []
    for row in range(1, rows):
        print("-----")
        data.append(
            [
                int(input(f"{col}-й столбец {row}-го ряда: "))
                for col in range(1, columns)
            ]
        )
    return Matrix(data)


if __name__ == "__main__":
    matrices = []

    count = input("Введите количество матриц для сложения: ")
    prompt_msg = "Введите размерность матриц через пробел (строки и столбцы): "
    dimensions = input(prompt_msg).split()

    # Инкрементируем указанные значения, чтобы повысить читаемость подсказок.
    count, rows, columns = (int(c) + 1 for c in (count, *dimensions))

    for i in range(1, count):
        print(f"\nЗаполняем {i}-ю матрицу...")
        matrix = fill_matrix(rows, columns)
        matrices.append(matrix)
        print("-----", f"{i}-я матрица: ", matrix, sep="\n")

    result = matrices[0]
    for i in range(1, len(matrices)):
        result += matrices[i]

    print("\nСумма матриц:", result, sep="\n")
