# BOTTOM-UP (tabulation)
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


# TOP-BOTTOM (memoization)
acc = []
def fib(n):
    if n < 0: return
    if n == 0 or n == 1:
        acc.insert(n, n)
    else:
        acc.insert(n, fib(n-2) + fib(n-1))

    return acc[n]

print(fib(4)) # 3
