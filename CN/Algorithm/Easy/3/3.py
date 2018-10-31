def isPalindrome(x):
    xx = x
    if x<0:
        return False
    result = 0
    while x!=0:
        result = result*10 + x%10
        x = x//10
    return xx==result
