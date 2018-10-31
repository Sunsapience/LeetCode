def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    Dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s)-1):
        if Dic[s[i]]<Dic[s[i+1]]:
            result -= Dic[s[i]]
        else:
            result += Dic[s[i]]
    return result+Dic[s[-1]]
