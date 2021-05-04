# determine each item’s number to include in a collection so that the total weight is less than or equal to a given limit.
# And also, the total value is maximum.
# The practical application of The knapsack problem algorithm is used in resource allocation. However, the decision-makers have
# to choose from a set of projects or tasks under a fixed budget or time constraint.
# KnapSack can be solved as well using a greedy algorithm or force brute

def knapSack(wMax, weights, vals, n):
    # init matrix:
    rows = n
    columns = wMax
    table = [[0 for i in range(columns + 1)] for j in range(rows + 1)]
    # [
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0]
    # ]

    for row, _ in enumerate(table):
        for column, _ in enumerate(table[row]):
            valCurrentItem = vals[row - 1]
            weightCurrentItem = weights[row - 1]

            if row == 0 or column == 0:
                continue
            elif weightCurrentItem <= column:
                bestValueForRemainingSpace = table[row - 1][column - weightCurrentItem]
                previousMax = table[row - 1][column]

                table[row][column] = max(
                    previousMax,                                  # same column but previous row
                    valCurrentItem + bestValueForRemainingSpace   # val of current item + best solution for rest of space (in previous row)
                )
            else:
                table[row][column] = table[row-1][column]

            print(table)



vals = [1500, 3000, 2000]
weights = [1, 4, 3]
wMax = 4
n  = 3

print(knapSack(wMax, weights, vals, n))

