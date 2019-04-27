def SimpleMode(arr):
    mode = 0 
    mostMode = 0
    numberStr = ""
    
    #numberStr = "".join(arr)
    modedict = {}
    
    for x in arr:
        
        if arr.count(x) > 1 and arr.count(x) > mostMode:
            mode = x 
            mostMode = arr.count(x)
            
    
    
    if mode == 0:
        return -1
    else:
        return mode
    

            
            
        
    
    

print(SimpleMode([1,2,2,3]))
    
    
    
    