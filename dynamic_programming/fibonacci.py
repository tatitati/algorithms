def fib(n):
    fibs = []
    for i in range(n+1):
        if i == 0 or i == 1:
            fibs.insert(i, i)
        else:
            fibs.insert(i, fibs[i-1] + fibs[i-2])

    print(fibs) # [0, 1, 1, 2, 3]
    return fibs.pop() # last item

print(fib(4)) # 3