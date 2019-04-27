def miniMaxSum(arr):
    arr.sort()
    minSum = sum(arr[:4])
    maxSum = sum(arr[1:])
    
    #print(minSum)
    #print(maxSum)
    
    print("%d %d" %(minSum,maxSum))


print(miniMaxSum([1 ,2 ,3 ,4 ,5]))