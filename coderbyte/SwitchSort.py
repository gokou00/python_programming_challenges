def SwitchSort(arr):
    arrSort = sorted(arr)
    count = 0 
    i = 0
    j = 0 
    
    
    while arr != arrSort:
        if arrSort[i] != arr[j]:
            idx = arr.index(arrSort[i])
            temp = arr[j]
            arr[j] = arr[idx]
            arr[idx] = temp
            count += 1
            j += 1
            i += 1
            continue
        
        j += 1
        i += 1
        
    
    return count





print(SwitchSort([5,4,3,1,2]))