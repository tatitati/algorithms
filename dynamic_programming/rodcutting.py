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
r = [0] + [-INF]*5

def top_down_rod(prices, cutSize):  
  if(r[cutSize] >= 0): return r[cutSize]

  maxVal = -INF
  for i in range(1, cutSize+1):
    maxVal = max(
      maxVal, 
      prices[i] + top_down_rod(prices, cutSize-i))

  r[cutSize] = maxVal
  print(r)
  return r[cutSize]

print(top_down_rod([0, 1, 4, 3, 7, 1], 5))
# [0, 1, -inf, -inf, -inf, -inf]
# [0, 1, 4, -inf, -inf, -inf]
# [0, 1, 4, 5, -inf, -inf]
# [0, 1, 4, 5, 8, -inf]
# [0, 1, 4, 5, 8, 9]
# 9











# def cutRodTopDown(prices, cutSize):
#     if(cutSize <= 0): return 0
#     max_val = -INF
#     for i in range(cutSize):
#         max_val = max(
#           max_val, 
#           prices[i] + cutRodTopDown(prices, cutSize - i - 1))

#     return max_val

# print(cutRodTopDown(
#   [0, 1, 4, 3, 7, 1], 
#   5
# ))









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