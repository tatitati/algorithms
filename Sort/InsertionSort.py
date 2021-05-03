def insertion_sort(nums):
    for idx, value in enumerate(nums):
        while idx > 0 and nums[idx - 1] > value:
            nums[idx] = nums[idx -1]
            idx = idx - 1
        nums[idx] = value

    return nums

array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
print(insertion_sort(array)) # [2, 3, 4, 6, 9, 14, 16, 21, 22, 27, 29, 30, 34, 36, 37, 39, 40, 41, 42, 47]