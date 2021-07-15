def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2  # dividing the array into two parts
        left = array[:mid]  # slicing to get left
        right = array[mid:]  # slicing to get right
        merge_sort(left)
        merge_sort(right)

        i = 0  # to keep track of left element in left
        j = 0  # to keep track of left element in right
        k = 0  # to keep track of left element in merged

# making comparisons and sorting

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

# sorting if there is no right array

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

# sorting if there is no left array

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


array = [4, 1, 3, 45, 6, 7, 1, 4, 6, 2, 9]
merge_sort(array)
print(array)
