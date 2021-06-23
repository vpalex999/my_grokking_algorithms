"""
Найти наибольшее число в списке рекурсивно.

Базовый случай: [x] - x -> max
"""

import unittest


def my_max(arr):
    if not arr:
        return
    if len(arr) == 1:
        return arr[0]
    _max = arr[0]
    _next_max = my_max(arr[1:])
    return _max if _max > _next_max else _next_max


class TestMaxInArr(unittest.TestCase):

    def test_max(self):
        test_case = [
            (my_max([]), None),
            (my_max([1]), 1),
            (my_max([1, 3, 2]), 3),
        ]

        for case in test_case:
            with self.subTest():
                result, expected = case
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
