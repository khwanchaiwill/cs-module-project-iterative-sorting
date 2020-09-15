def linear_search(arr, target):
    # Your code here
    # search target in the arr[]
    for i in range(len(arr)):
        if arr[i] == target: # if target is found return the index of that target
            return i # i is the index of target we are looking at

    return -1   # not found # if not found we return the -1 index


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0 
    right = len(arr) -1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle -1
        else:
            left = middle + 1

    return -1  # not found

    # left = 0 
    # right = len(arr) -1
    # while right >= left:
    #     middle = (left + right) // 2
    #     if arr[middle] == target:
    #         return middle
    #     elif arr[middle] < target:
    #        left = middle + 1
    #     else:
    #         right = middle - 1

    # return -1  # not found


arr = [3, 4, 6, 16 , 26, 28, 52, 55]

print(binary_search(arr, 52))