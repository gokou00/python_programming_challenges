def ArrayRotation(arr):
    num = arr[0]
    
    for i in range(num):
        temp = arr.pop(0)
        arr.append(temp)
        
        
    # convert to a string     
    
    return arr



print(ArrayRotation( [2, 3, 4, 1, 6, 10] ))



