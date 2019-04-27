def arrayPreviousLess(items):
    finalArr = []
    finalArr.append(-1)
    least = 0
    found = False
    
    

    
    for i in range(1,len(items)):
        #print(i)
        for j in range(i-1,-1,-1):
            #print(i, "i")
            #print(j, "idx")
            if items[j] < items[i]:
                finalArr.append(items[j])
                found = True
                break
        if found:
            found = False
        else:
            finalArr.append(-1)
            

    
    
    return finalArr


print(arrayPreviousLess([68, 135, 101, 170, 125] ))
    