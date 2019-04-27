def launchSequenceChecker(systemNames,stepNumbers):
    testmap = {}
    
    for x in systemNames:
        testmap[x] = []
    
    
    for i in range(len(systemNames)):
        testmap[systemNames[i]].append(stepNumbers[i])
    
    
    for x in testmap.values():
        checker = isIncrease(x)
        if checker == False:
            return False
    
    return True
    
    
    
    
    
    #print(testmap)

def isIncrease(arr):
    isIncreasing = True
    
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            continue
        else:
            return False
    
    
    return isIncreasing
    

print(launchSequenceChecker( ["stage_1", "stage_1", "stage_2", "dragon"], [2, 1, 12, 111]))