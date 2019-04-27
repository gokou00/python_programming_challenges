import itertools
def closest_sum(ints, num):
    # your solution goes here
    arraySum = []
    for L in range(0, len(ints)+1):
    #for L in range(3):
        for subset in itertools.combinations(ints, L):
            if len(subset) == 3:
                
                arraySum.append(sum(subset))
            
    
    
    print(arraySum)
    
    sumDict = {}
    
    for x in arraySum:
        sumDict[x] = 0
        
    
    for x in sumDict:
        sumDict[x] = x - num
        
    ansArray = []
    
    for key,val in sumDict.items():
        ansArray.append(abs(val))
        
    #ansArray.sort()
    
    temp = min(ansArray)
    print(temp)
    
    for key,val in sumDict.items():
        if abs(val) == temp:
            return key
        
        
    print(sumDict)
    

print(closest_sum([5, 1, -8, -9, -2],3))

    
    