def ChangingSequence(arr):
    
    #print(len(arr))
    
    isIncreaing = False
    
    if arr[1] > arr[0]:
        isIncreaing = True
        
        
    if isIncreaing:
        for i in range(0,len(arr)-1):
        #print(i)
            if arr[i+1] > arr[i]:
                continue
            else:
                return i
    elif not isIncreaing:
        for i in range(0,len(arr)-1):
            if arr[i+1] < arr[i]:
                #print("test")
                continue
            else:
                return i
        
    

            
    return -1
    
    

print(ChangingSequence([3, 2, 1, 0, -1, -2, 10]))
        