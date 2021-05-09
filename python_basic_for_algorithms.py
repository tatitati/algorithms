'''
common pieces of code across all the algorithms in python.
'''

# print arrays quickly in strings
print("my car is ",  ["a", "b", "c", "d"], "and is in ", ["a", "b", "c", "d"]) # my car is  ['a', 'b', 'c', 'd'] and is in  ['a', 'b', 'c', 'd']

# infinity
# ========
print(float("inf")) # inf

# swap values
# ===========
a = ["a", "b", "c", "d"]
a[1], a[2] = a[2], a[1] # ['a', 'c', 'b', 'd']
print(a)


# range
# =====
print(list(range(5)))  	  # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4]


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
# up to...
print(a[:0]) # []
print(a[:1]) # a
print(a[:-1]) # ['a', 'b', 'c', 'd']
# from...
print(a[2:]) # c d e
# between...
print(a[1:-1]) # b c d
# between jumping...
print(a[1:-1:2]) # b d


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
print(a.pop(0)) # a, a now is ["b", "c"]

# stack
# =====
a = []
a.append("a")
a.append("b")
a.append("c")
print(a.pop()) # c, a now is ['a', 'b']