INF = float("inf");

# lengths = [0, 1, 2, 3, 4, 5]
# prices =  [0, 2, 3, 7, 8, 9] 

# # Bottom-up (tabulation)
# memo = 0
# def rodBottomUp(cutLength):
#     for i in range(cutLength+1):
#         if i == 0 or i == 1:
#             memo.insert(i, prices[i])
#         else:
#             max(
#                 prices[i],
#                 max(pric[:i-1] + memo[]), 

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











def cutRodTopDown(prices, cutSize):
    if(cutSize <= 0): return 0
    max_val = -INF
    for i in range(0, cutSize):
        max_val = max(
          max_val, 
          prices[i] + cutRodTopDown(prices, cutSize - i - 1))

    return max_val

print(cutRodTopDown(
  [0, 1, 4, 3, 7, 1], 
  3
))









# r = [0] + [-1*INF]*5


# def bottom_up_rod_cutting(c, n):
#   r = [0]*(n+1)
#   r[0] = 0

#   for j in range(1, n+1):
#     print("---- %s" % j)      
#     maximum_revenue = -1*INF
#     for i in range(1, j+1):
#       maximum_revenue = max(maximum_revenue, c[i] + r[j-i])
#       print("c[%s] + r[%s-%s] = %s + %s" % (i, j, i, c[i], r[j-i]))
#       print("max_revenue %s" % maximum_revenue)
#     r[j] = maximum_revenue
#   return r[n]

# if __name__ == '__main__':
#   #array starting from 1, element at index 0 is fake
#   # c = [0, 2, 3, 7, 8, 9] # --> 11
#   c = [0, 1, 4, 3, 7, 1]#  --> 9
#   print(bottom_up_rod_cutting(c, 4))