"""

Runtiime complexity is O(n^2) as we go throgh the list twice (two loops)

"""


def insertion_sort_iter(array):
    for i in range(1, len(array)):
        current_element = array[i]
        sorted_element = i - 1
        while sorted_element >= 0 and current_element < array[sorted_element]:
            array[sorted_element + 1] = array[sorted_element]
            sorted_element -= 1
        array[sorted_element+1] = current_element
    return array


array = [6, 2, 24, 5, 6, 2, 1, 6, 24, 56, 2, 87, 13, 90]
print("Iteravtive:", insertion_sort_iter(array))


def insertion_sort_recursive(array, n):
    if n <= 1:
        return
    insertion_sort_recursive(array, n-1)
    current_element = array[n-1]
    sorted_element = n-2
    while sorted_element >= 0 and array[sorted_element] > current_element:
        array[sorted_element+1] = array[sorted_element]
        sorted_element -= 1
    array[sorted_element+1] = current_element


array = [6, 2, 24, 5, 6, 2, 1, 6, 24, 56, 2, 87, 13, 90]
n = len(array)
insertion_sort_recursive(array, n)
print("Resursive:", array)
