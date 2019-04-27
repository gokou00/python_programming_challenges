import itertools
def PermutationStep(num):
    numStr = str(num)
    numStrArry = list(numStr)
    permlist = list(itertools.permutations(numStrArry))
    
    for x in permlist:
        temp = "".join(x)
        tempNum = int(temp)
        if tempNum > num:
            return tempNum
        
    
    #print(permlist)
    
    return -1



print(PermutationStep(41352))
    
    
    