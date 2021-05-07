

# lengths = [0, 1, 2, 3, 4, 5]
prices =  [0, 2, 3, 7, 8, 9] 

# Bottom-up (tabulation)
# acc = 0
# def rodBottomUp(cutLength):
#     for i in range(cutLength+1):
#         if i == 0 or i == 1:
#             acc.insert(i, prices[i])
#         else:
#             max(
#                 prices[i],
#                 max(acc[:i-1]),

#             )


# print(rodBottomUp(4)) # 9


# TOP-DOWN (memoization)
# INF = 100000;
# r = [0] + [-1*INF]*5

# def top_down_rod_cutting(prices, n):
#   if(r[n] >= 0):
#     return r[n]

#   maximum_revenue = -1*INF

#   for i in range(1, n+1):
#     maximum_revenue = max(maximum_revenue, prices[i] + top_down_rod_cutting(prices, n-i))

#   r[n] = maximum_revenue
#   return r[n]

# print(top_down_rod_cutting(prices, 3))





