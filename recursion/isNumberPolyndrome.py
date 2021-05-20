# https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/

def isNumberPolindrome(num):
    resultCurrentIteration = True if num[0] == num[-1] else False

    # base case
    if len(num) == 2: return resultCurrentIteration

    return resultCurrentIteration and isNumberPolindrome(num[1:-1])    


print(isNumberPolindrome([1, 2, 3, 4])) # false
print(isNumberPolindrome([2, 0, 0, 2])) # true