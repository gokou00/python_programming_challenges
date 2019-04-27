def MeanMode(arr):
    mean = 1
    mode = 0
    total = 0
    temp = 0
    
    arrmap = {}
    for x in arr:
        total += x
        
    mean = total / len(arr)
    
    for x in arr:
        arrmap[x] = 0
        
    for x in arr:
        arrmap[x]+=1
    
    for key,val in arrmap.items():
        if val > temp and val >= 2:
            temp = val
            mode = key
            
    
    print(mode)
    print(mean)
    
    if mode == mean:
        return 1
    else:
        return 0
    
    
print(MeanMode([1,2,3]))
        