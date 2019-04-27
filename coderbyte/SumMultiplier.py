import itertools
def SumMultiplier(arr):
    total = sum(arr)
    total *= 2
    arrList = list(itertools.combinations(arr,2))
    
    for x in arrList:
        if x[0]*x[1] > total:
            return "true"
            
    
    #print(arrList)
    #print(total)
    
    return "false"


print(SumMultiplier([1, 1, 2, 10, 3, 1, 12]))
    