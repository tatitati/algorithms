"""
An insertion sort compares values in turn, starting with the second value in the list. If this value is greater
than the value to the left of it, no changes are made. Otherwise this value is repeatedly moved left until it meets a
value that is less than it. The sort process then starts again with the next value. This continues until the end of
the list is reached.
"""

def insertion_sort(nums):
    for i, value in enumerate(nums):
        if(i > 0 and nums[i-1] > value): # needed back-swap
            for j in reversed(range(i)):
                if nums[j] > value:
                    nums[j], nums[j+1] = nums[j+1], nums[j] # swap

    return nums


array = [4, 22, 41, 40, 27, 30, 36]
print(insertion_sort(array)) # [4, 22, 27, 30, 36, 40, 41]