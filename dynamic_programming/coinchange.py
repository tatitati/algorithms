'''
Given a value N, if we want to make change for N cents, and 
we have infinite supply of each of S = { S1, S2, .. , Sm} valued 
coins, how many ways can we make the change? The order of 
coins doesn\’t matter.

Examples
=========
* for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. 

*For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
So the output should be 5.
'''
def coinChange( coins, amount ):
	Opt = [0 for i in range(0, amount+1)]
	n = len(coins)

	for i in range(1, amount+1):
		smallest = float("inf")
		for j in range(0, n):
			if (coins[j] <= i): 
				smallest = min(smallest, Opt[i - coins[j]]) 
		Opt[i] = 1 + smallest 
	return Opt[amount]

print(coinChange([1, 2, 3],  4))