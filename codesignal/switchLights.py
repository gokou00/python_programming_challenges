def switchLights(a):
    
    for i in range(0,len(a)):
        
        if a[i] == 1:
            a[i] = 0
            
            for j in range(i-1,-1,-1):
                if a[j] == 1:
                    a[j] = 0
                else:
                    a[j] = 1
    
    
    return a
    
    


print(switchLights([1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1 ]))