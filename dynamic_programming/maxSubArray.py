# https://leetcode.com/problems/maximum-subarray/


def maxSubArray(nums):
	memo = []
	for i, _ in enumerate(nums):
		if i == 0: 
			memo.append(nums[i])
			continue
			
		memo.append(max(
			memo[i-1] + nums[i],
			nums[i]
		))
		
			
	print(memo)
	return max(memo)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubArray([5,4,-1,7,8])) # 23
                
            
                