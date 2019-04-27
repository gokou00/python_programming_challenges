def ThirdGreatest(strArr):
    stringArrMap = {}
    strArrLength = []
    orderedArray = []
    
    for x in strArr:
        strArrLength.append(len(x))
    
    strArrLength.sort()
    
    for x in strArr:
        stringArrMap[x] = len(x)
        
    
    for i in range(0,len(strArr)):
        for j in range(0,len(strArr)):
            if strArrLength[i] == len(strArr[j]) and strArr[j] not in orderedArray:
                orderedArray.append(strArr[j])
                
                
    
    
    isdiff = True
    
    for i in range(0,len(orderedArray)-1):
        if len(orderedArray[i]) == len(orderedArray[i+1]):
            isdiff = False
    
    
    if isdiff:
        return orderedArray[0]
        
        
    isSame = True
    
    for i in range(0,len(orderedArray)-1):
        if len(orderedArray[i]) != len(orderedArray[i+1]):
            isdiff = False
            
    
    if isSame:
        return orderedArray[len(orderedArray)-1]
    
    return orderedArray[1]
        
        
    
        
    

    
    
    print(orderedArray)
        
    
    
    
    print(stringArrMap)
    


print(ThirdGreatest(["bat","cat","mat"]))    