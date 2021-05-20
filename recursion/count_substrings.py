# https://www.geeksforgeeks.org/recursive-solution-count-substrings-first-last-characters/

def recursiveSearch(text, searchLetter):	
	resultIteration = 1 if text[0] == searchLetter else 0	

	# base case
	if len(text) == 1:
		return resultIteration
	
	return resultIteration + recursiveSearch(text[1:], searchLetter)


def main(text):
	result = 0
	for i, _ in enumerate(text):
		result += recursiveSearch(text[i:], text[i])

	return result



print(main(["a", "b", "a"])) # 4
print(main(["a", "b", "c", "a", "b"])) # 7
print(main(["a", "b", "c", "a", "b", "a", "c"])) # 12
