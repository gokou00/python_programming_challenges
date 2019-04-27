def sumDigits(num):
    
    total = 0
    pop = 0
    
    while num > 0:
        pop = num % 10
        total += pop
        num /=10
        
    
    return total


def mostFrequentDigitSum(n):
    digitArr = []
    digitMap = {}
    
    
    
    while n > 0:
        temp = sumDigits(n)
        
        digitArr.append(temp)
        
        n = n - temp
    
    
    digitArr.sort()
    
    for x in digitArr:
        if x not in digitMap:
            digitMap[x] = 1
        else:
            digitMap[x] += 1
    
    
    largest = 0 
    mostfreq = 0
    
    #print(digitArr)
    
    for x in digitArr:
        if digitMap[x] >= largest:
            largest = digitMap[x]
            mostfreq = x
    
    return mostfreq
        
        
    
    
    
print(mostFrequentDigitSum(99999))   
    
    
    

