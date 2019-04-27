def countSumOfTwoRepresentations(n, l, r):
    arr = {}
    arr2 = []
    for i in range(l,r+1):
        for j in range(l,r+1):
            if i + j == n:
                arr2.append(i)
                arr2.append(j)
                arr2.sort()
                statement = str(arr2[0])+ "+" +str(arr2[1])
                arr[statement] = 1
                #statement = ""
                arr2 = []
    
    
    return len(arr)



print(countSumOfTwoRepresentations(24,12,12))
