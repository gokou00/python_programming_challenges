def FoodDistribution(arr):
    numSandwhich = arr.pop(0)
    arr.sort()
    count = 0
    diffArry = []
    total = 0
    
    while numSandwhich != 0 and count < len(arr)-1:
        temp = abs(arr[count +1] - arr[count])
        numSandwhich -= temp
        diffArry.append(temp)
        count += 1
    
    
    
    print(diffArry)
    
    for x in diffArry:
        total = abs(total) -  x
    
    #print(total)
    
    return abs(total)



print(FoodDistribution([20, 5, 4, 1]))
