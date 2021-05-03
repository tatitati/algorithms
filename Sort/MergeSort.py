# This algorithm is one of the most efficient techniques to sort an array and it is implemented using the divide and conquer approach.

# - An initial array is divided into two roughly equal parts. If the array has an odd number of elements, one of those "halves" is by
# one element larger than the other.
# - The subarrays are divided over and over again into halves until you end up with arrays that have only one element each.
# - Then you combine the pairs of one-element arrays into two-element arrays, sorting them in the process. Then these sorted pairs
# are merged into four-element arrays, and so on until you end up with the initial array sorted.


def mergeSort(arr):
    if len(arr) > 1:

        #Finding the middle of the array
        r = len(arr)//2

        #Dividing array into two halves
        leftArray = arr[:r]
        rightArray = arr[r:]

        #Calling mergesort function on subparts of array
        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        #Copying data to temp arrays leftArray[] and rightArray[]
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1


        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1

        return arr

print(mergeSort([6, 5, 12, 10, 9, 1 ])) # [1, 5, 6, 9, 10, 12]