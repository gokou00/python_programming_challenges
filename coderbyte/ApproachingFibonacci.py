def ApproachingFibonacci(arr):
    arrSum = sum(arr)
    fibArr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,17711, 28657, 46368, 75025, 121393, 196418, 317811]
    diff1 = 0
    diff2 = 0
    #print(arrSum)
    
    if arrSum in fibArr:
        return 0
    
    
    for i in range(len(fibArr)):
        if arrSum < fibArr[i]:
            diff1 = fibArr[i] - arrSum
            diff2 = arrSum - fibArr[i-1]
            return min(diff2,diff1)
        
    
    
print(ApproachingFibonacci([1,20,2,5]))