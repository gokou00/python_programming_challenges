def GasStation(strArr):
    num = int(strArr.pop(0))
    
    total = 0
    isImpossible = False
    storageArr = []
    
    for i in range(num):
        for j in range(num):
            #print(strArr)
            idx = strArr[j].find(":")
            total += int(strArr[j][:idx])
            total -= int(strArr[j][idx+1:])
            #print(total)
            
            if total < 0:
                isImpossible = True
                break
        
        
        if isImpossible:
            isImpossible = False
            temp = strArr.pop(0)
            strArr.append(temp)
            total = 0
        else:
            storageArr.append(i + 1)
            temp = strArr.pop(0)
            strArr.append(temp)
            total = 0
            
            
    if len(storageArr) == 0:
        return "impossible"
    
    #print(storageArr)
    storageArr.sort()
    return storageArr[0]



print(GasStation(["4","1:1","2:2","1:2","0:1"]))