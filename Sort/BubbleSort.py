# Bubble sort is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in
# which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
# This algorithm is not suitable for large data sets as its average and worst case
# complexity are of Ο(n2) where n is the number of items.

def bubbleSort(nums):
    madeChanges = None
    while(madeChanges != False):
        madeChanges = False

        for idx, num in enumerate(nums):
            if idx == len(nums)-1: continue
            elif nums[idx] > nums[idx+1]:
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx] # swap
                madeChanges = True
    return nums


nums = [64, 34, 25, 12, 22, 11, 90]

print(bubbleSort(nums)) # [11, 12, 22, 25, 34, 64, 90]
