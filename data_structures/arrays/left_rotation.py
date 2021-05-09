def rotLeft(numbers, rotations):
    result = [0]*len(numbers)
    for idx, val in enumerate(numbers):
        result[idx-rotations] = val
        
    return result


print(rotLeft([1,2,3,4,5,6,7,8], 5)) # [6, 7, 8, 1, 2, 3, 4, 5]

