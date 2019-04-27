def LargestPair(num):
    numStr = str(num)
    largest = 0
    
    for i in range(len(numStr)-1):
        temp = numStr[i] + numStr[i+1]
        if int(temp) > largest:
            largest = int(temp)
        
            
    
    
    return largest


print(LargestPair(363223311))