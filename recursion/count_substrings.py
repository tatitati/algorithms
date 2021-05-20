# https://www.geeksforgeeks.org/recursive-solution-count-substrings-first-last-characters/

def countSubstrings(text, searchLetter):	
	# base case
	if len(text) == 1:
		return 1 if text[0] == searchLetter else 0

	return 1 + text[]






countSubstrings(["a", "b", "a"]) # 4
countSubstrings(["a", "b", "c", "a", "b"]) # 7
countSubstrings(["a", "b", "c", "a", "b", "a", "c"]) # 12
