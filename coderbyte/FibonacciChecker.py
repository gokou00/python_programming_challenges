def FibonacciChecker(num):
    total = num + 1
    fibArr = [0] * total
    fibArr[0] = 0
    fibArr[1] = 1
    
    for i in range(2,num + 1):
        fibArr[i] = fibArr[i-1] + fibArr[i-2]
    
    if num in fibArr:
        return "yes"
    else:
        return "no"
    
    #return fibArr[num]


print(FibonacciChecker(54))