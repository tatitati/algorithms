# Bubble sort is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in
# which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
# This algorithm is not suitable for large data sets as its average and worst case
# complexity are of Ο(n2) where n is the number of items.


def bubbleSort1(nums):
    done = False
    while(done == False):
        done = True
        for i, _ in enumerate(nums):
            if i == 0: continue
            if nums[i-1] > nums[i]: 
                nums[i], nums[i-1] = nums[i-1], nums[i]
                done = False
                continue            

    return nums

print(bubbleSort1([64, 34, 25, 12, 22, 11, 90])) # [11, 12, 22, 25, 34, 64, 90]




def bubbleSort2(nums):
    for _, _ in enumerate(nums):
        for j, _ in enumerate(nums[:-1]):            
            if nums[j] > nums[j+1]: nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

print(bubbleSort2([64, 34, 25, 12, 22, 11, 90])) # [11, 12, 22, 25, 34, 64, 90]