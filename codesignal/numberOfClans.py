def numberOfClans(divisors, k):
    numDict = {}
    
    for i in range(1,k+1):
        numDict[i] = ""
    
    
    for i in numDict:
        for j in divisors:
            if i % j == 0:
                numDict[i] += str(j) + "is a div"
            else:
                numDict[i] += str(j) + "is not a div"
    
    
    #print(numDict)
    
    
    groups = []
    
    test4 = {}
    
    for key,val in numDict.items():
        test4[val] = 0
    
    return len(test4)

print(numberOfClans([1, 3] , 10))
    
    