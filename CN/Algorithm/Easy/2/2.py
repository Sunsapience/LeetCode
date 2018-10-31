def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    xx=x
    result = 0
    k = 1 if x>=0 else -1
    x=k*x
    while x!=0:
        temp= result*10 + x%10
        if k==1  and ((result > pow(2,31)//10) or ((result == pow(2,31)//10) and (x%10 >7))):
            return 0
        if k==-1 and ((result > pow(2,31)//10) or ((result == pow(2,31)//10) and (x%10 >8))):
            return 0
        result = temp
        x = x//10
    return k*result 
