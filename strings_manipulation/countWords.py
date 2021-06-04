# Complexity
# ==========
# It seems that because of only one FOR loop is O(n), but the "in" keyword of python use 
# linear-search internally, which is O(n), so the whole problem is O(n^2)

text = "my car is red blue and my house is white and blue is the sky like my car but not like trees or foxes but indeed like water"
tokens = text.split(" ")

acc = {}

for token in tokens:
	if token in acc: acc[token] += 1
	else: acc[token] = 1

print(acc) # {'my': 3, 'car': 2, 'is': 3, 'red': 1, 'blue': 2, 'and': 2, 'house': 1, 'white': 1, 'the': 1, 'sky': 1, 'like': 3, 'but': 2, 'not': 1, 'trees': 1, 'or': 1, 'foxes': 1, 'indeed': 1, 'water': 1}