def ArithGeo(arr):
    #test arith
    isArith = True
    isGeo = True
    
    arith = arr[1] - arr[0]
    
    for i in range(0,len(arr)-1):
        if arr[i+1] - arr[i] != arith:
            isArith = False
            break
        
        
    geo = arr[1] / arr[0]
    
    for i in range(0,len(arr)-1):
        if arr[i+1] / arr[i] != geo:
            isGeo = False
            
            
    
    if isArith:
        return "Arithmetic"
    elif isGeo:
        return "Geometric"
    else:
        return -1
        
print(ArithGeo([2,4,16,24]))