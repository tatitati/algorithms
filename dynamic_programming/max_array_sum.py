

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
        
print(result)
print(max(result))
    
