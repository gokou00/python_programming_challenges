def rotateString(A, B):
    count = 0
    
    tempAArr = list(A)
    if A == B:
        return True
    
    while count < 5:
        temp = tempAArr.pop(0)
        tempAArr.append(temp)
        
        newA = "".join(tempAArr)
        if newA == B:
            return True
        
        count+=1
    
    
    return False



print(rotateString('abcde','abced'))


        
        