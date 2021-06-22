"""
Функция суммирования чисел в списке с использованием рекурсии.
"""
import unittest


def my_sum(arr):
    if not arr:
        return 0
    return arr[0] + my_sum(arr[1:])


class TestSum(unittest.TestCase):

    def test_sum(self):
        test_case = [
            (sum([1, 2]), 3),
            (sum([]), 0),
            (sum([1]), 1)
        ]

        for case in test_case:
            with self.subTest():
                result, expected = case
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
