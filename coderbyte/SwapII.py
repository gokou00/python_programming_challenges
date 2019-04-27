def SwapII(string):
    numStack = []
    stringArr = list(string)
    idx = -1
    finalStr = ""
    
    #loop to swap the numbers 
    for i in range(len(stringArr)):
        if (stringArr[i] >= "0" and stringArr[i] <= "9") and len(numStack) == 0:
            numStack.append(stringArr[i])
            idx = i
            continue
        if idx != -1 and stringArr[i].isalnum() == False:
            idx = -1
            numStack.pop()
            continue
        if idx != -1 and (stringArr[i] >= "0" and stringArr[i] <= "9") and stringArr[i-1].isalpha():
            print("test")
            temp = stringArr[i]
            stringArr[i] = numStack.pop()
            stringArr[idx] = temp
            idx = -1
        
        #print(numStack)
        #print(idx)
    
    
    #print(numStack)
    #print(stringArr)
    string = "".join(stringArr)
    print(string)
    
    for x in string:
        if x.islower():
            finalStr += x.upper()
            continue
        if x.isupper():
            finalStr += x.lower()
            continue
        
        finalStr += x
    
    print(finalStr)
    return finalStr
        
    
    
    
    

print(SwapII("6Hello4 -8World, 7 yes3"))
        
        