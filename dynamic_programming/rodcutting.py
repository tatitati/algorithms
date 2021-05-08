INF = float("inf");

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

print(top_down_rod([0, 2, 3, 7, 8, 9], 5))
# [0, 2, -inf, -inf, -inf, -inf]
# [0, 2, 4, -inf, -inf, -inf]
# [0, 2, 4, 7, -inf, -inf]
# [0, 2, 4, 7, 9, -inf]
# [0, 2, 4, 7, 9, 11]
# 11
print(top_down_rod([0, 1, 4, 3, 7, 1], 5))
# [0, 1, -inf, -inf, -inf, -inf]
# [0, 1, 4, -inf, -inf, -inf]
# [0, 1, 4, 5, -inf, -inf]
# [0, 1, 4, 5, 8, -inf]
# [0, 1, 4, 5, 8, 9]
# 9





# BOTTOM-UP (tabulation)

r = [0] + [-INF]*5
def bottom_up_rod(prices, cutSize):
  r = [0]*(cutSize+1)

  for j in range(1, cutSize+1):
    maxVal = -INF
    for i in range(1, j+1):
      maxVal = max(
        maxVal, 
        prices[i] + r[j-i]
      )

    r[j] = maxVal
    print(r)
  return r[cutSize]


print(bottom_up_rod([0, 2, 3, 7, 8, 9], 5))
# [0, 2, 0, 0, 0, 0]
# [0, 2, 4, 0, 0, 0]
# [0, 2, 4, 7, 0, 0]
# [0, 2, 4, 7, 9, 0]
# [0, 2, 4, 7, 9, 11]
# 11
print(bottom_up_rod([0, 1, 4, 3, 7, 1], 5)) 
# [0, 1, 0, 0, 0, 0]
# [0, 1, 4, 0, 0, 0]
# [0, 1, 4, 5, 0, 0]
# [0, 1, 4, 5, 8, 0]
# [0, 1, 4, 5, 8, 9]
# 9