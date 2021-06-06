# Complexity
# ==========
# It seems that because of only one FOR loop is O(n), but the "in" keyword of python use 
# linear-search internally, which is O(n), so the whole problem is O(n^2)

words = ["my",  "car",  "is", "a", "red", "blue", "car"]

counters = {}

for word in words:
	if word in counters: counters[word] += 1
	else: counters[word] = 1

print(counters) # {'my': 1, 'car': 2, 'is': 1, 'a': 1, 'red': 1, 'blue': 1}