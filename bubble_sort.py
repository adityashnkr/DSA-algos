def bubble_sort_iter(array):
    swap_flag = 0
    n = len(array)
    for i in range(n):
        for i in range(0, n-i-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap_flag = 1
        if swap_flag == 0:
            swap_flag = 0
    return array


def bubble_sort(array):
    swap_falg == 0


a = [1, 2, 3, 4, 5, 6, 1]
print(bubble_sort(a))
