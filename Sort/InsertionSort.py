def insertion_sort(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue

    return array

array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
print(insertion_sort(array)) # [2, 3, 4, 6, 9, 14, 16, 21, 22, 27, 29, 30, 34, 36, 37, 39, 40, 41, 42, 47]