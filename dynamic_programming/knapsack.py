# determine each item’s number to include in a collection so that the total weight is less than or equal to a given limit.
# And also, the total value is maximum.
# The practical application of The knapsack problem algorithm is used in resource allocation. However, the decision-makers have
# to choose from a set of projects or tasks under a fixed budget or time constraint.
# KnapSack can be solved as well using a greedy algorithm or force brute

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50 # max total weight
n = len(val)
print(knapSack(W, wt, val, n)) # 100(20kg) + 120(30kg) = 220