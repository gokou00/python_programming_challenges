def arrayConversion(inputArray):
    arr = []
    count  = 1 
    
    while len(inputArray) != 1:
        if count % 2 == 0:
            temp = []
            for i in range(0,len(inputArray)-1,2):
                temp.append(inputArray[i] * inputArray[i+1])
            
            inputArray = temp[:]
        else:
            temp = []
            for i in range(0,len(inputArray)-1,2):
                temp.append(inputArray[i] + inputArray[i+1])
            inputArray = temp[:]
        #print(inputArray)
        count += 1
    
    return inputArray



print(arrayConversion([3, 3, 5, 5] ))
            
        
    