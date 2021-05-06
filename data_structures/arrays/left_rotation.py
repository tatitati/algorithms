def rotLeft(listNumbers, rotations):
    for x in range(rotations):
        listNumbers = listNumbers[1:] + listNumbers[:1]
    return listNumbers


print(rotLeft([1,2,3,4,5,6,7,8], 5)) # [6, 7, 8, 1, 2, 3, 4, 5]

