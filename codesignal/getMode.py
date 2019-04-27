def m(arr):
    largest = 0
    index = -1
    arrDict = {}
    
    
    for x in arr:
        if x not in arrDict:
            arrDict[x] = 1
        else:
            arrDict[x] += 1
    
    for idx,val in enumerate(arr):
        if arrDict[x] >= largest:
            largest = arrDict[x]
            index = idx
    
    if index == -1:
        return -1
    else:
        return arr.pop(index)
            


def getMode(elements, ops):
    temp = []
    final = []
    
    for x in ops:
        if x == 0 and elements:
            temp.append(elements.pop(0))
        elif x == 1:
            test = m(temp)
            if test == -1:
                continue
            else:
                final.append(test)
    
    
    return final
    

print(getMode([7, 2, 1, 7, 6, 7] ,[1, 1, 0, 0, 0, 0] ))
            
    