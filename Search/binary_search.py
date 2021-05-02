def binary_search_iterative(arr, x):
    low = 0 # low idx
    high = len(arr) - 1 # high idx
    mid = 0 # mid idx

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)

    else:
        return -1


arr = [ 2, 3, 4, 8, 10, 30, 40, 60 ]
print(binary_search_iterative(arr, 4)) # element present at index: 3
print(binary_search_recursive(arr, 0, len(arr)-1, 4)) # element present at index: 3

