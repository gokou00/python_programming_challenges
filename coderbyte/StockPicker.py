def StockPicker(arr):
    
    if arr == sorted(arr,reverse=True):
        return -1
    
    
    largest = 0
    buy = 0
    sell = 0
    smallest = 0
    profit = []
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                temp = arr[j] - arr[i]
                if temp > largest:
                    largest = temp
        
        profit.append(largest)
    
    
                
                
    #print(profit)
    
    profit.sort()
    
    return profit[-1]

            

                
            
            
        
    
    
    
    #return largest




print(StockPicker(        [10,23,12,5,10,45]  ))
        
        
        