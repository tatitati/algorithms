'''
common pieces of code across all the algorithms in python.
'''

# infinity
# ========
print(float("inf")) # inf

# range
# =====
print(list(range(5)))  # [0, 1, 2, 3, 4]


# for + len + range
# =================
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