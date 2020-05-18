# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for n in range(i, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n

        # TO-DO: swap
        # Your code here
        # swapping values
        swapped_value = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = swapped_value
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    run = True
    while run:
        run = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                swapped_value = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = swapped_value
                run = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(arr1))
