
def bribe(q):
	origQ = range(1, len(q+1))

	bribes = 0
	for idx, val in enumerate(q):
		if val > origQ[idx]:
			bribes



print(bribe([4, 1, 2, 3]))