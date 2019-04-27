def ArithGeoII(arr):
    arth = abs(arr[1])-abs(arr[0])
    geo = abs(arr[1])//abs(arr[0])
    
    #print(arth)
    print(geo)
    
    isArth = True
    isGeo = True
    
    for i in range(1,len(arr)-1):
        if abs(arr[i]) + arth != abs(arr[i+1]):
            isArth = False
            break
    
    if isArth:
        return "Arithmetic"
    
    
    for i in range(1,len(arr)-1):
        if abs(arr[i]) * geo != abs(arr[i+1]):
            isGeo = False
            break
    
    if isGeo:
        return "Geometric"
    
    return -1
    
    
            



print(ArithGeoII([2,4,16,24]))
