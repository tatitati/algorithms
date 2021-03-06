# This algorithm is one of the most efficient techniques to sort an array and it is implemented using the divide and conquer approach.

# - An initial array is divided into two roughly equal parts. If the array has an odd number of elements, one of those "halves" is by
# one element larger than the other.
# - The subarrays are divided over and over again into halves until you end up with arrays that have only one element each.
# - Then you combine the pairs of one-element arrays into two-element arrays, sorting them in the process. Then these sorted pairs
# are merged into four-element arrays, and so on until you end up with the initial array sorted.

import math

# COMPLEXITY:
# ==========
# Algorithmic Paradigm: Divide and Conquer
# θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.

# Notes:
# ======
# Merge sort algorithm requires an additional memory space of 0(n) for the temporary array.
# It goes through the whole process even if the array is sorted.

# Is useful to learn an algorith to sort two arrays. 
# Once you know how to do this, you just need to split the arrays and sort them with this function. 
# The learning process is much softer in this way
def mergeAndSort(left, right):
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

print(mergeAndSort([5, 7, 10], [3, 6]))




def split(arr):     
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
    
    left = split(left)
    right = split(right)

    return mergeAndSort(left, right)

print(split([6, 5, 12, 10, 9, 1, 14 ])) # [1, 5, 6, 9, 10, 12, 14]