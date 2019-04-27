def Superincreasing(arr):
    for i in range(0,len(arr)):
        if i == 0:
            continue
        #print(i)
        #print(arr[0:i])
        
        if arr[i] > sum(arr[0:i]):
            #print(arr[0:i])
            continue
        else:
            return False

    
    return True
    

print(Superincreasing([1,2,5,10]))