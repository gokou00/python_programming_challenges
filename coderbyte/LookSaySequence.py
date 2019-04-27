def LookSaySequence(num):
    numStr = str(num)
    count = 0
    buildStr = ""
    isDone = False
    i = 0 
    
    while i < len(numStr):
        for  j in range(i,len(numStr)):
           
            if numStr[i] == numStr[j]:
                count += 1
            elif numStr[i] != numStr[j]:
                break
            
            
        
        temp = str(count) + numStr[i]
        buildStr += temp
        if count == len(numStr[i:]):
            break
        else:
            i = i + count
             

            count = 0
        #print(buildStr)
            
    
    #print(buildStr)
    return buildStr


print(LookSaySequence(44))