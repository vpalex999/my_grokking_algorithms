"""
Функция подсчёта количества чисел в списке с использованием рекурсии.
"""
import unittest


def my_count(arr):
    if not arr:
        return 0
    return 1 + my_count(arr[1:])


class TestCountArr(unittest.TestCase):

    def test_count(self):
        test_case = [
            (my_count([1, 2]), 2),
            (my_count([]), 0),
            (my_count([1]), 1)
        ]

        for case in test_case:
            with self.subTest():
                result, expected = case
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
