"""

Understanding heapify: 
    Looking at just leaves it is alreadya a min/max heap 
    So we start from the second last level and swap the elements wrt min/max heap
    Time complexity: O(n) for heapify and for heap sort O(nlogn)

"""


def heapify(array, rooted, length):
    # setting the largest element as the rooted element or the element we look down from
    largest = rooted
    left = 2 * rooted + 1  # left child index
    right = 2 * rooted + 2  # right child index

    # to check if left exists and if is grater than the rooted element
    if left < length and array[largest] < array[left]:
        largest = left

    # to check if right exists and if is grater than the rooted element
    if right < length and array[largest] < array[right]:
        largest = right

    # swap the rooted element if needed
    if largest != rooted:
        array[rooted], array[largest] = array[largest], array[rooted]

        heapify(array, rooted, length)


def heap_sort(array):
    length = len(array)

    # 1 Step: Build Max-Heap
    for i in range(length//2, -1, -1):
        heapify(array, i, length)  # will return Max-Heap

    # 2 Step Remove elements one-by-one till only one element is left
    for i in range(length-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)


array = [12, 11, 13, 5, 6, 7]
heap_sort(array)
print(array)
