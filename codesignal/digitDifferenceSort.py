#use a dict with [int]= int[]
def digitDifferenceSort(a):
    ans = []
    ranking = {}
    
    for x in a:
        tempStr = str(x)
        tempArr = list(tempStr)
        tempArr.sort()
        #if len(tempArr)
        num = int(tempArr[-1]) - int(tempArr[0])
        if num not in ranking:
            ranking[num] = []
            ranking[num].append(x)
        else:
            ranking[num].append(x)
    testArr = ranking.keys()
    
    testArr.sort()
    
    for x in testArr:
        if len(ranking[x]) == 1:
            ans = ans + ranking[x]
        else:
            ans = ans + ranking[x][::-1]
    
    return ans
            

print(digitDifferenceSort([152, 23, 7, 887, 243]))
        