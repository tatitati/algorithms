# This algorithm is one of the most efficient techniques to sort an array and it is implemented using the divide and conquer approach.

# - An initial array is divided into two roughly equal parts. If the array has an odd number of elements, one of those "halves" is by
# one element larger than the other.
# - The subarrays are divided over and over again into halves until you end up with arrays that have only one element each.
# - Then you combine the pairs of one-element arrays into two-element arrays, sorting them in the process. Then these sorted pairs
# are merged into four-element arrays, and so on until you end up with the initial array sorted.

import math

# COMPLEXITY:
# Algorithmic Paradigm: Divide and Conquer
# 

# Is useful to learn an algorith to sorto two arrays. 
# Once you know how to do this, you just need to split the arrays and sort them with this function. 
# The learning process is much softer in this way
def merge(left, right):
    a = len(left) - 1
    b = len(right) - 1
    result = [0]*(len(left) + len(right))
    writeIdx = len(result)-1
    

    while a >= 0  and b >= 0:
        if left[a] >= right[b]:
            result[writeIdx] = left[a]
            a -= 1
        elif left[a] < right[b]:
            result[writeIdx] = right[b]
            b -= 1

        writeIdx -= 1
    
    if a >= 0: result[:a+1] = left[:a+1]
    elif b >= 0: result[:b+1] = right[:b+1]

    return result

print(merge([5, 7, 10], [3, 6]))




def mergeSort(arr):     
    # divide and sort

    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr = arr[::-1]
        return arr

    middle = math.ceil(len(arr)/2)
    left = arr[:middle]
    right = arr[middle:]
    
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

print(mergeSort([6, 5, 12, 10, 9, 1, 14 ])) # [1, 5, 6, 9, 10, 12, 14]