'''
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
Note Each toy can be purchased only once.

Example:
prices = 1, 2, 3, 4
K = 7
The budget is 7 units of currency. 
He can buy items that cost [1, 2, 3] for 6, or [3, 4] for 7 units. The maximum is 3 items. 
'''

def maximumToys(prices, budget):
    prices.sort()
    toys = 0
    spent = 0
    for price in prices:
        if price<budget and spent + price < budget: 
            toys += 1
            spent += price
        else:
            return toys



print(maximumToys([3, 7, 2, 9, 4], 7)) # [3,1,4,2] == $6
# print(maximumToys([3,1,4,2], 7)) # [3,1,4,2] == $6
