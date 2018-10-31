def isPalindrome(x):
    xx = x
    if x<0:
        return False
    result = 0
    while x!=0:
        temp = result*10 + x%10
        result = temp
        x = x//10
    return True if xx==result else False
