def wordPattern(pattern, string):
    patternDict ={}
    stringDict ={}
    patternStr = ""
    stringStr = ""
    stringList = string.split(" ")
    count = 1
    
    for x in pattern:
        if x not in patternDict:
            patternDict[x] = count
            count += 1
    
    for x in pattern:
        patternStr += str(patternDict[x])
    
    count = 1
    
    for x in stringList:
        if x not in stringDict:
            stringDict[x] = count
            count += 1
    
    for x in stringList:
        stringStr += str(stringDict[x])
        
    #print(patternStr)
    #print(stringStr)
    
    
    return patternStr == stringStr

print(wordPattern( "abba" , "dog dog dog dog" ))
    
    
    
        
            