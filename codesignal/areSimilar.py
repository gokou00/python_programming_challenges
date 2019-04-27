def areSimilar(a, b):
    if a == b:
        return True
    
    
    aMap = {}
    bMap = {}
    
    if len(aMap) != len(bMap):
        return False
    
    for x in a:
        if x not in aMap:
            aMap[x] = 1
        else:
            aMap[x] += 1
    
    
    for x in b:
        if x not in bMap:
            bMap[x] = 1
        else:
            bMap[x] += 1
    
    
    for x in aMap:
        if x not in bMap:
            return False
        if bMap[x] != aMap[x]:
            return False
            
        
    count = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    
    
    if count <= 2:
        return True
    else:
        return False
        

print(areSimilar([1, 2, 3] ,[1, 2, 3] ))