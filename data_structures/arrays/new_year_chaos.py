
def bribe(q):
	origQ = range(1, len(q)+1)

	bribe = 0
	for idx, val in enumerate(q):
		if val - origQ[idx] > 2:
			print("too chaotic")
			return
		else:			
			bribe += val - origQ[idx]

	print(bribe)



# print(bribe([4, 1, 2, 3])) # too chaotic
# bribe([1, 2, 3, 5, 4, 6, 7, 8]) # 1
# bribe([2, 1, 5, 3, 4]) # 3 --> 5 bribed twice, and 2 bribed one
# bribe([2, 5, 1, 3, 4]) # too chaotic
bribe([1, 2, 5, 3, 7, 8, 6, 4]) # 
