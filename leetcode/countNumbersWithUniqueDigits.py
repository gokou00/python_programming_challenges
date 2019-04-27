def countNumbersWithUniqueDigits(n):
    total = 10 ** n
    
    #print(set("1"), set("1"))
    count = 0
    
    for i in range(total):
        numStr =  str(i)
        numStrSet = set(numStr)
        
        if len(numStr) != len(numStrSet):
            count +=1
        
    
    return total - count
            
        


print(countNumbersWithUniqueDigits(2))