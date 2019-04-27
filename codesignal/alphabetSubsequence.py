def alphabetSubsequence(s):
    
    #letterMap = {}
    
    for x in s:
        if s.count(x) > 1:
            return False
    
    strArr = list(s)
    
    strArrCopy = strArr[:]
    
    strArrCopy.sort()
    
    for i in range(len(strArr)):
        if strArr[i] != strArrCopy[i]:
            return False
    
    
    return True



print(alphabetSubsequence("qa" ))
    