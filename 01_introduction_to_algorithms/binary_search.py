"""
Бинарный поиск.
Работает только с отсортированными элементами списка.
Количество итераций вычисляется логарифмом по основанию 2: log2(8) = 3(найдёт за три шага).
Время поиска - логарифмическое O(Log n).
"""


def binary_search(src_arr, item):
    low = 0
    high = len(src_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        quess = src_arr[mid]

        if quess == item:
            return mid
        if quess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


arr = [1, 3, 5, 7, 8, 9]    # отсортированный список

print(binary_search(arr, 3))    # => 1
print(binary_search(arr, -1))   # => None
