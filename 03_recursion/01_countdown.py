"""
Простая рекурсия
"""


def countdown(i):
    if i <= 0:  # base case
        return 0
    else:  # recursive case
        print(i)
        return countdown(i - 1)


countdown(5)
