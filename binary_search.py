"""

Array needs to be sorted.
Run time complexity is O(log(n)) as  each time we cut our search space in half. Everytime array size doubles the # of iteration increases by 1 


"""

def binanry_search(array, left, right, val):
    if left > right:
        return -1
    mid = (left+right)//2
    if val == array[mid]:
        return mid
    elif val > array[mid]:
        return binanry_search(array, mid+1, right, val)
    else:
        return binanry_search(array, left, mid-1, val)


a = [1, 2, 3, 4, 5, 6]
left = 0
right = len(a) - 1
val = 4
print("Recursion:", + binanry_search(a, left, right, val))


def binanry_search_iter(array, val):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left+right)//2
        if val == array[mid]:
            return mid
        elif val > array[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1


print(binanry_search_iter(a, val))
