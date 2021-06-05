
def binarysearch1(arr, target, lowIdx = None, highIdx = None):
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
	

print(binarysearch1([ 2, 3, 4, 8, 10, 30, 40, 60, 100 ], 4)) # element present at index: 3