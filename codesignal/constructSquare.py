import itertools
def constructSquare(s):
    squareNums = []
    
    strDict = {}
    squareNumsDict = {}
    permStr = set(list(itertools.permutations(list(s))))
    
    for x in range(105000):
        temp = x ** 2
        #print(temp)
        
        tempStr = convert(temp)
        squareNums.append(tempStr)
        squareNumsDict[tempStr] = temp
    
    
    count = 1
    largest = 0
    patternArr = []
    
    for x in permStr:
        tempStr = "".join(x)
        
        tempStrPattern = convert(tempStr)
        patternArr.append(tempStrPattern)
    
    
    
    squareArr = []
    
    for x in patternArr:
        if x in squareNumsDict:
            squareArr.append(squareNumsDict[x])
            if int(squareNumsDict[x]) > largest:
                largest = int(squareNumsDict[x])
    
    
    #squareArr.sort()
    if squareArr:
        return largest
    else:
        return -1
    
    
    
    #print(squareArr[-1])
    
    #print(patternArr)    
    #print(permStr)
    #print(strPattern)
    #print(squareNums)
    
    #if strPattern in squareNumsDict:
        #return squareNumsDict[strPattern]
    #else:
        #return -1
    
    
    #return strPattern in squareNums
        
    








def convert(num):
    numStr = str(num)
    strBuild = ""
    numDict = {}
    count = 1
    
    for x in numStr:
        if x not in numDict:
            numDict[x] = count
            count += 1
    
    
    for x in numStr:
        strBuild += str(numDict[x])
    
    
    return strBuild
        
            
    
print(constructSquare(  "aaaabbcde"  ))