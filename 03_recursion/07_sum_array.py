"""
Find sum in list
"""


def summ_array(arr):
    if not arr:
        return 0
    return arr[0] + summ_array(arr[1:])


print(summ_array([2, 6, 1]))
