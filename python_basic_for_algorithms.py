'''
common pieces of code across all the algorithms in python.
'''

# print 
# =====
# concat arrays quickly in strings
print("my car is ",  ["a", "b", "c", "d"], "and is in ", ["a", "b", "c", "d"]) # my car is  ['a', 'b', 'c', 'd'] and is in  ['a', 'b', 'c', 'd']

# increment number
# ================
# in python you cannot do a++
a = 5
a += 1
print(a) # 6

# infinity
# ========
print(float("inf")) # inf

# swap values
# ===========
a = ["a", "b", "c", "d"]
a[1], a[2] = a[2], a[1] # ['a', 'c', 'b', 'd']
print(a)

# sort() vs sorted()
# ==================
# sort() update the original array, it return always None
a = [8, 5, 6, 2, 4, 1]
a.sort()
print(a) # [1, 2, 4, 5, 6, 8] 
# sorted() instead return a new one sorted
b = [8, 5, 6, 2, 4, 1]
print(sorted(b)) # [1, 2, 4, 5, 6, 8]
print(b) # [8, 5, 6, 2, 4, 1]

# how can we map() in an array?
# =============================
a = [8, 5, 6, 2, 4, 1]
arr = [x-1 for x in a]
print(arr) # [7, 4, 5, 1, 3, 0]


# range
# You cannot create a reverted range: range(5, 1), wrong
# =====
print(list(range(5)))  	  # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(reversed(range(1, 5))))  # [4, 3, 2, 1]


# for + len + range VS for + enumerate
# ====================================
# you will see this loop a lot. Trick: is much easier to read in the second way (with enumerate)
for idx in range(len(["a", "b", "c", "d", "e"])):
	print(idx) # 0 1 2 3 4 

for idx, _ in enumerate(["a", "b", "c", "d", "e"]):
	print(idx) # 0 1 2 3 4 

# array slices
# ============
a = ["a", "b", "c", "d", "e"]
# ending at...
print(a[:0]) # []
print(a[1:]) # ["b", "c", "d", "e"]
print(a[:1]) # a
print(a[:-1]) # ['a', 'b', 'c', 'd']
# starting at...
print(a[2:]) # c d e
# between, slice...
print(a[1:3]) # b c
print(a[1:-1]) # b c d
# between jumping...
print(a[1:-1:2]) # b d

print(a[-3]) # c


# init matrixes
# =============
print([0]*5) 		# [0, 0, 0, 0, 0]
print([3] + [0]*4)  # [3, 0, 0, 0, 0]

print([ 0 for j in range(5)]) # [0, 0, 0, 0, 0]
print([[ 0 for x in range(3)] for y in range(5)]) 
# [
# 	[0, 0, 0], 
# 	[0, 0, 0], 
# 	[0, 0, 0], 
# 	[0, 0, 0], 
# 	[0, 0, 0]
# ]

# queue
# =====
a = []
a.append("a")
a.append("b")
a.append("c")
print(a.pop(0)) # a, a == ["b", "c"]

# stack
# =====
a = []
a.append("a")
a.append("b")
a.append("c")
print(a.pop()) # c, a == ['a', 'b']