def countingSort(arr):
	count = [0]*(max(arr)+1)
	acc = [0]*(max(arr)+1)
	output = [0]*(max(arr)+1)

	for i, val in enumerate(arr):
		count[val] += 1

	for i, val in enumerate(count):
		if i == 0: acc[0] = count[0]
		else: acc[i] = count[i] + acc[i-1]

	for i, val in enumerate(arr):
		resultIdx = acc[val]-1
		output[resultIdx] = val
		acc[val] -= 1

	return output

print(countingSort([4, 2, 2, 8, 3, 3, 1]))