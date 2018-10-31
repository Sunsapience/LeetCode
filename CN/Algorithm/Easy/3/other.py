def isPalindrome(self, x):
    if x<0 or (x%10==0 and x!=0):
        return False
    result = 0
    while x>result:
        result = result*10 + x%10
        x = x//10
    return result==x or result//10==x
