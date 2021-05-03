def insertion_sort(nums):
    for i, value in enumerate(nums):
        if(i > 0 and nums[i-1] > value): # needed back-swap
            for j in reversed(range(i)):
                if nums[j] > value:
                    nums[j], nums[j+1] = nums[j+1], nums[j] # swap

    return nums


array = [4, 22, 41, 40, 27, 30, 36]
print(insertion_sort(array)) # [4, 22, 27, 30, 36, 40, 41]