"""
Бустрая сортировка методом разделяй и влавствуй

Базовый случай:
[] -> []
[x] -> [x]

"""

import unittest


def my_quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return my_quicksort(less) + [pivot] + my_quicksort(greater)


class TestMaxInArr(unittest.TestCase):

    def test_max(self):
        test_case = [
            (my_quicksort([]), []),
            (my_quicksort([1]), [1]),
            (my_quicksort([10, 5, 2, 3]), [2, 3, 5, 10]),
            (my_quicksort([10, 6, 10]), [6, 10, 10])
        ]

        for case in test_case:
            with self.subTest():
                result, expected = case
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
