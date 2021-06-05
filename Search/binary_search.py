def binary_search_iterative(arr, x):
    low = 0 # low idx
    high = len(arr) - 1 # high idx
    mid = 0 # mid idx

    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] == x: return mid # base condition
        if arr[mid] < x: low = mid + 1
        elif arr[mid] > x: high = mid - 1
        

    return -1


def binary_search_recursive(arr, target, lowIdx = None, highIdx = None):
	# 1. define base case
	if lowIdx != None and highIdx != None and lowIdx == highIdx: 
		if arr[lowIdx] == target: return lowIdx
		else: return -1

	# 2. define next recursion
	if lowIdx == None or highIdx == None:		
		highIdx = len(arr) - 1
		lowIdx = 0

	mid = (lowIdx + highIdx) // 2
	if target == arr[mid]: return mid
	if target <  arr[mid]: return binarysearch1(arr, target, lowIdx, mid-1) # search to the right
	elif target > arr[mid]: return binarysearch1(arr, target, mid+1, highIdx) # search to the right
	

arr = [ 2, 3, 4, 8, 10, 30, 40, 60 ]
print(binary_search_iterative(arr, 4)) # element present at index: 3
print(binary_search_recursive(arr, 0)) # element present at index: 3

