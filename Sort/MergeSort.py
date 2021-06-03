# This algorithm is one of the most efficient techniques to sort an array and it is implemented using the divide and conquer approach.

# - An initial array is divided into two roughly equal parts. If the array has an odd number of elements, one of those "halves" is by
# one element larger than the other.
# - The subarrays are divided over and over again into halves until you end up with arrays that have only one element each.
# - Then you combine the pairs of one-element arrays into two-element arrays, sorting them in the process. Then these sorted pairs
# are merged into four-element arrays, and so on until you end up with the initial array sorted.

import math


def mergeSort(arr):
    
    print(middle)
    print(middle2)


mergeSort([6, 5, 12, 10, 9, 1, 14 ]) # [1, 5, 6, 9, 10, 12, 14]