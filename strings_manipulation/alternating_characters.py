

def alternatingCharacters(text):	
	deletions = 0 
	chars = list(text)
	acc = ""
	for i, c in enumerate(chars):
		if i == 0: acc += c
		elif c == chars[i-1]: 
			deletions += 1
		else:
			acc += c		

	return deletions

print(alternatingCharacters("AAAA")) # 3


