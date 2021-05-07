"""
determine each items number to include in a collection so that the total weight is less than or equal to a given limit.
And also, the total value is maximum.
The practical application of The knapsack problem algorithm is used in resource allocation. However, the decision-makers have
to choose from a set of projects or tasks under a fixed budget or time constraint.
KnapSack can be solved as well using a greedy algorithm or force brute
"""

def knapSack(wMax, weights, vals, n):
    table = [[0 for i in range(wMax + 1)] for j in range(n + 1)]
    # [
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0]
    # ]

    for y, _ in enumerate(table):
        for x, _ in enumerate(table[y]):
            valCurrentItem = vals[y - 1]
            weightCurrentItem = weights[y - 1]

            if y == 0 or x == 0: continue
            elif weightCurrentItem <= x:
                bestValueForRemainingSpace = table[y - 1][x - weightCurrentItem]
                previousMax = table[y - 1][x]

                table[y][x] = max(
                    previousMax,                                  # same column but previous row
                    valCurrentItem + bestValueForRemainingSpace   # val of current item + best solution for rest of space (in previous row)
                )
            else: table[y][x] = table[y-1][x]

    return table

vals = [1500, 3000, 2000]
weights = [1, 4, 3]
wMax = 4
n  = 3

print(knapSack(wMax, weights, vals, n))

