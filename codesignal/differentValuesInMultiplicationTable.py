def differentValuesInMultiplicationTable(n, m):
    arr = []
    for i in range(1,n+1):
        for j in range(1,m+1):
            arr.append(i*j)
    
    
    return len(set(arr))


print(differentValuesInMultiplicationTable(4,4))