import random
import sys
import typing
import unittest
from unittest.mock import patch


@patch("builtins.print")  # print будет писать в mock_print вместо sys.stdout
class TestSalary(unittest.TestCase):
    """Тесты для упр.1 (расчёт зарплаты)."""

    @patch("builtins.print")  # иначе print напишет в sys.stdout при импорте
    def setUp(self, mock_print):
        from Homework_4.ex1 import salary  # исключаем побочные эффекты

        self.salary = salary
        self.test_argv = [str(i) for i in (sys.argv[0], 8.2, 1000, 200)]

    def test_correct_input(self, mock_print):
        with patch("Homework_4.ex1.argv", self.test_argv):
            self.salary()

        time, rate, bonus = map(float, self.test_argv[1:])
        mock_print.assert_called_with(f"Salary - {time*rate + bonus}")

    def test_incorrect_input(self, mock_print):
        for test_argv in (
            [],
            self.test_argv[:1],
            self.test_argv + [42],
        ):
            with patch("Homework_4.ex1.argv", test_argv):
                self.salary()
            mock_print.assert_called_with("Некорректный ввод! Введите 3 числа.")


@patch("builtins.print")
class TestFilteredList(unittest.TestCase):
    """Тесты для упр.2 (фильтрация списка)."""

    def test_correct_input(self, mock_print):
        from Homework_4.ex2 import my_list, res_list

        rng = range(1, len(my_list))
        out = [my_list[i] for i in rng if my_list[i] > my_list[i - 1]]

        self.assertEqual(res_list, out)
        mock_print.assert_called_with(out)


@patch("builtins.print")
class TestFactorial(unittest.TestCase):
    """Тесты для упр.7 (нахождение факториала)."""

    @patch("builtins.input")
    @patch("builtins.print")
    def setUp(self, mock_input, mock_print):
        from Homework_4.ex7 import factorial

        self.factorial = factorial
        self.wrong_values = ("True", "!5", "e", "3.14")

    def test_correct_input(self, mock_print):
        in_val = "3"
        out = self.factorial(int(in_val))
        self.assertIsInstance(out, typing.Iterable)

    def test_incorrect_input(self, mock_print):
        value = random.choice(self.wrong_values)
        with self.assertRaises(ValueError):
            self.factorial(int(value))

@patch("builtins.print")
class TestExponentiation(unittest.TestCase):
    """Тесты для упр.4 (возведение в степень)."""

    @patch("builtins.input")
    @patch("builtins.print")
    def test_correct_input(self, mock_print):
        from Homework_3.ex_4 import my_func_1
        self.my_func_1 = my_func_1
        in_val_1 = "7"
        in_val_2 = "4"
        out = self.my_func_1(int(in_val_1), int(in_val_2))
        self.assertEqual(int('2401'), out)
        #mock_print.assert_called_with(out)



if __name__ == "__main__":
    unittest.main()
