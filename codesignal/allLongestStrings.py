def allLongestStrings(inputArray):
    largest = 0
    finalArr = []
    
    for x in inputArray:
        if len(x) > largest:
            largest = len(x)
    
    
    
    for x in inputArray:
        if len(x) == largest:
            finalArr.append(x)
    
    return finalArr




print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
    
    
    