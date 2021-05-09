
def bribe(q):
	bribe = 0
	memoBribers = [0]*len(q)
	for idx, val in enumerate(q):				
		if val - (idx+1) > 2:
			print("Too chaotic")
			return
		
		for j in q[:idx]:
			if j > val:
				bribe += 1 

	print(bribe)



bribe([4, 1, 2, 3]) # too chaotic
bribe([1, 2, 3, 5, 4, 6, 7, 8]) # 1
bribe([2, 1, 5, 3, 4]) # 3 --> 5 bribed twice, and 2 bribed one
bribe([2, 5, 1, 3, 4]) # too chaotic
bribe([1, 2, 5, 3, 7, 8, 6, 4]) # 7
