def DistinctList(arr):
    total = 0
    numDict = {}
    for x in arr:
        if x not in numDict:
            numDict[x] = 1
        else:
            numDict[x] +=1
    
    
    #print(numDict)
    
    for val in numDict.values():
        if val > 1:
            total += val -1
    
    #print(total)
    return total


print(DistinctList([100,2,101,4]))