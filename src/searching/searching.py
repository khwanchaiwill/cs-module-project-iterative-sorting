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
    low = 0 
    high = len(arr) -1
    while low <=high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        if guess > target:
            high = middle -1
        else:
            low = middle + 1

    return -1  # not found
