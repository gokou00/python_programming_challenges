def ElementMerger(arr):
    tempArry = []
    
    while len(arr) > 1:
        for i in range(len(arr)-1):
            #print(arr[i+1], arr[i])
            #print(arr[i])
            tempArry.append(abs(arr[i+1] - arr[i]))
        
        arr = []
        #print(tempArry)
        arr = tempArry
        #print(arr)
        tempArry = []
    
    
    print(arr)


print(ElementMerger([1, 1, 1, 2]))