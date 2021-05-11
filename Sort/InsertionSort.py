"""
An insertion sort compares values in turn, starting with the second value in the list. If this value is greater
than the value to the left of it, no changes are made. Otherwise this value is repeatedly moved left until it meets a
value that is less than it. The sort process then starts again with the next value. This continues until the end of
the list is reached.
"""

def insertion_sort(nums):
    for i, val in enumerate(nums):
        if i == 0: continue
        if nums[i-1] > nums[i]:        
            for j in reversed(range(i)):
                try: # in this way I don't need to check if is the last iteration or the index doesnt exist                                            
                    if nums[j] > nums[j+1]: nums[j+1], nums[j] = nums[j], nums[j+1] # swap
                finally:
                    continue

    return nums

print(insertion_sort([4, 22, 41, 40, 27, 30, 36])) # [4, 22, 27, 30, 36, 40, 41]