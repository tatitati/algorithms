
def checkMagazine(magazine, note):
	dictio = {}
	for word in list(magazine.split(" ")):
		if word in dictio: dictio[word] += 1 
		else: dictio[word] = 1
		

	print(dictio)
	for i, word in enumerate(list(note.split(" "))):		
		if word not in dictio.keys() or dictio[word] <=  0:
			print("No")
			return
		
		if dictio[word] > 0:
			dictio[word] -= 1
			
	print("Yes")
	return



checkMagazine(
	"give me one grand today night",
	"give one grand today"
)

checkMagazine(
	"two times three is not four",
	"two times two is four"
)