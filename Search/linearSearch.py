
# Complexity
# ===========
# Average case time complexity: O(N)
# Best case (you find it at the start) time complexity: O(1)
# Worst case (you find it at the end) time complexity: O(N)
# Space complexity: O(1)


def linearSearch(words, target):
	for i, word in enumerate(words):
		if word == target: return i

linearSearch(["tree", "car", "castle", "ocean", "universe", "hello", "something"], "hello")
