def pairOfShoes(shoes):
    arrSize = []
    
    for x in shoes:
        if x[0] == 0:
            arrSize.append(x[1])
    
    
    
    for x in shoes:
        if x[0] == 1:
            if x[1] in arrSize:
                idx = arrSize.index(x[1])
                del arrSize[idx]
            elif x[1] not in arrSize:
                return False
    
    print(arrSize)
    return len(arrSize) == 0


print(pairOfShoes([[1,1], 
 [1,1], 
 [1,3], 
 [0,2], 
 [0,2], 
 [0,1]] ))