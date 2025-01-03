from typing import List

arr = [3, 6, 1, 9]

def find_lower_index(arr):
    lower = arr[0]
    lower_index = 0

    for i in range(1, len(arr)):
        if arr[i] < lower:
            lower = arr[i]
            lower_index = i
    return lower_index

print(find_lower_index(arr))

def selection_sort(arr: List[int]):
    ordered_arr = []
    for i in range(len(arr)):
        lower = find_lower_index(arr)
        ordered_arr.append(arr.pop(lower))

    return ordered_arr

print(selection_sort(arr))