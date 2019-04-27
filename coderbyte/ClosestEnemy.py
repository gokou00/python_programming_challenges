def ClosestEnemy(arr):
    if 2 not in arr:
        return 0
    
    idx = arr.index(1)
    count = 0
    
    
    for i in range(idx + 1,len(arr)):
        count +=1
        if arr[i] == 2:
            return count  
    
    
    count = 0
    
    for i in range(idx-1 ,0,-1):
        #print(arr[i])
        count +=1
        if arr[i] == 2:
            return count
    
        
    


print(ClosestEnemy(         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]      ))