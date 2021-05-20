def fib(n):
    if(n == 0 or n == 1): return n
    return fib(n-1) + fib(n-2)


print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(4)) # 3
