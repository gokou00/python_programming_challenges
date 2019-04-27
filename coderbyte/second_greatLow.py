def SecondGreatLow(arr):
    arr.sort()
    
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return str(arr[0]) + " " + str(arr[1])
        else:
            return str(arr[1]) + " " + str(arr[0])
    
    first = ""
    last = ""
            
    
    
    if arr[1] == arr[0]:
        first = str(arr[2])
    else:
        first = str(arr[1])
    
    if arr[-1] == arr[-2]:
        last = str(arr[-3])
    else:
        last = str(arr[-2])
        
    
    return first + " " + last
    
        
            
   


print(SecondGreatLow([7, 7, 12, 98, 106]))         