def fib(num):
    #efficient way to get fib. I included the % 10 to get the last digit
    total = num + 1
    fibArr = [0] * total
    fibArr[0] = 0
    fibArr[1] = 1
    
    for i in range(2,num + 1):
        fibArr[i] = fibArr[i-1] + fibArr[i-2]
    
    return fibArr[num] % 10

print(fib(89))