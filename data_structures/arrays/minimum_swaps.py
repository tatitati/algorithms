
def minimumSwaps(arr):
    res = 0
    arr = [x-1 for x in arr]
    value_idx = {x:i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        if i != x:
            to_swap_idx = value_idx[i]
            arr[i], arr[to_swap_idx] = i, x
            value_idx[i] = i
            value_idx[x] = to_swap_idx
            res += 1
    print(res)
    return res



# print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))
print(minimumSwaps([4, 3, 1, 2]))
