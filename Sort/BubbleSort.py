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
