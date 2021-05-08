def counting(n):
    print(n)
    if n <= 0 or n == 1: return 1
    else: return counting(n-2)
        


counting(9) # 9 7 5 3 1