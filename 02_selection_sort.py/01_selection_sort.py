"""
Алгоритмы сортировки
"""


def selection_sort(arr):
    """Сортировка выбором по возрастанию O(n^2)."""
    selected_arr = []

    while True:
        curr_index = None
        # найти наименьший элемент
        for el_index in range(len(arr)):
            if curr_index is None:
                curr_index = el_index
            if arr[curr_index] > arr[el_index]:
                curr_index = el_index
                continue
        # перенести его в новый массив
        if curr_index is not None:
            selected_arr.append(arr[curr_index])
            del arr[curr_index]
            curr_index = None
        else:
            break

    return selected_arr


my_arr = [5, 3, 6, 2, 10]
print(selection_sort(my_arr))
