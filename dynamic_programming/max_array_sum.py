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

# nums = [3, 7, 4, 6, 5] 
# Expected 13

# nums = [2, 1, 5, 8, 4]
# Expected 11

nums = [3, 5, -7, 8, 10]
# Expected 15

result = []
for idx, _ in enumerate(nums):
    print(result)
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
        
print(result)      # [3, 5, 5, 13, 15]
print(max(result)) #15
    
