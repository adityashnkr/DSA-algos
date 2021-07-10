"""

Runtiime complexity is O(n^2) as there are 2 for loops

"""


def bubble_sort_iter(array, n):
    swap_flag = 0
    for i in range(n):
        for i in range(0, n-i-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap_flag = 1
        if swap_flag == 0:
            break


def bubble_sort_recu(array, n):
    for i in range(n-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    if n > 1:
        bubble_sort_recu(array, n-1)


array = [6, 2, 24, 5, 6, 2, 1, 6, 24, 56, 2, 87, 13, 90]
n = len(array)
bubble_sort_iter(array, n)
print("Iterative:", array)
array = [6, 2, 24, 5, 6, 2, 1, 6, 24, 56, 2, 87, 13, 90]
bubble_sort_recu(array, n)
print("Recursive:", array)
