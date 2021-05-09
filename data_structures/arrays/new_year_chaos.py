'''
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker 
indicating their initial position in the queue from to. Any person can bribe the person directly in front of 
them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of 
bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example
q = [1 2 3 5 4 6 7 8]
If person 5 bribes person 4 the queue will look like this. Only 1 bribe is required. Print 1.
q = [4 1 2 3]
Person 4 had to bribe 3 people to get to the current position. Print Too chaotic. 
'''

def bribe(q):
	bribe = 0
	memoBribers = [0]*len(q)
	for idx, val in enumerate(q):				
		if val == (idx + 1): continue
		if val - (idx+1) > 2:
			print("Too chaotic")
			return
			
		if j > val:
			return bribe += 1 

		bribe += bribe(q[:idx])		
		for j in q[:idx]:
			if j > val:
				bribe += 1 

	print(bribe)



bribe([4, 1, 2, 3]) # too chaotic
bribe([1, 2, 3, 5, 4, 6, 7, 8]) # 1
bribe([2, 1, 5, 3, 4]) # 3 --> 5 bribed twice, and 2 bribed one
bribe([2, 5, 1, 3, 4]) # too chaotic
bribe([1, 2, 5, 3, 7, 8, 6, 4]) # 7
