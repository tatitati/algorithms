'''
common pieces of code across all the algorithms in python
'''

print(list(range(5)))  # [0, 1, 2, 3, 4]


# you will see this loop a lot. Trick: is much easier to read in the second way (with enumerate)
for idx in range(len(["a", "b", "c", "d", "e"])):
	print(idx) # 0 1 2 3 4 

for idx, _ in enumerate(["a", "b", "c", "d", "e"]):
	print(idx) # 0 1 2 3 4 


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
