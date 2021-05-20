# https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/

def isNumberPolindrome(num):
    if len(num) == 2: return num[0] == num[len(num)-1]
    if num[0] == num[len(num)-1]:
        return isNumberPolindrome(num[1:-1])
    else: return False


print(isNumberPolindrome([1, 2, 3, 4])) # false
print(isNumberPolindrome([2, 0, 0, 2])) # true