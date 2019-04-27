#use ordered set

def newNumeralSystem(number):
    alphaStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaMap = {}
    numberMap = {}
    finalAns = []
    
    for i in range(len(alphaStr)):
        alphaMap[alphaStr[i]] = i
        
    for i in range(len(alphaStr)):
        numberMap[i] = alphaStr[i]
        
    #print(alphaMap)
    #print(numberMap)
    target = alphaMap[number]
    testArr = []

    
    for x in alphaStr:
        key1 = x
        val1 = alphaMap[x]
        
        find = target - val1
        
        if find in numberMap:
            testArr.append(key1)
            testArr.append(numberMap[find])
            testArr.sort()
            
            strBuild = testArr[0]
            strBuild += " + "
            strBuild += testArr[1]
            if strBuild not in finalAns:
                finalAns.append(strBuild)
                
            testArr = []
    
    
    return(finalAns)
    
    


print(newNumeralSystem("W"))
            
        