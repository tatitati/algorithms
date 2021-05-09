'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. 
Calculate the sum of that subset. It is possible that the maximum sum is, the case when 
all elements are negative.

Example
The following subsets with more than
element exist. These exclude the empty subset and single element subsets which are also valid.

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
'''

def maxSum(nums):
    result = []
    for idx, _ in enumerate(nums):
        if idx == 0:
            result.append(nums[0])
        elif idx == 1:
            result.append(max(nums[0], nums[1]))
        else:
            result.insert(idx, max(
                nums[idx],
                max(result),
                result[idx-2] + nums[idx]
            ))
            
    return max(result)
            
        
print(maxSum([3, 5, -7, 8, 10])) # 15
    
