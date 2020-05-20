def linear_search(arr, target):
    # Your code here
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # indexes in the array
    left = 0
    right = len(arr) - 1

    while right >= left:
        # find the midpoint
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
