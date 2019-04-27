def LongestIncreasingSequence(arr):
    dparr = []
    
    temp = arr
    while len(temp) > 0:
        dparr.append(count(temp))
        temp = temp[1:]
        
    dparr.sort()    
    print(dparr)
    
    return dparr[-1]

def count(arr):
    length = 0
    arr1 = []
    
    for i in range(len(arr)):
        if i == 0:
            arr1.append(arr[i])
            continue
            
            
        if arr[i] > arr1[-1]:
            arr1.append(arr[i])
        
        arr1.sort()
        
    print(arr1)    

    
    return len(arr1)
            
    

print(LongestIncreasingSequence([10, 12, 4, 6, 100, 2, 56, 34, 79, 45, 33, 12, 45, 67, 89]))