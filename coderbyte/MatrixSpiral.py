def MatrixSpiral(strArr):
    arr = []
    arr1 = []
    for x in strArr:
        temp = list(x)
        del temp[0]
        del temp[-1]
        
        strTemp = "".join(temp)
        tempArr = strTemp.split(",")
        arr.append(tempArr)
    
    
    k = 0
    l = 0
    m = len(arr)
    n = len(arr[0])
    while(k < m  and l < n ):
        for i in range(l,n):
            arr1.append(arr[k][i].strip())
        
        k += 1
        
        for i in range(k,m):
            arr1.append(arr[i][n-1].strip())
        
        n-=1
        
        if(k<m):
            for i in range(n-1,(l-1),-1):
                arr1.append(arr[m-1][i].strip())
            
            m-=1
        
        if(l < n):
            for i in range(m-1,k-1,-1):
                arr1.append(arr[i][l].strip())
            l += 1
    
    
    return ",".join(arr1)   
    
    
    


print(MatrixSpiral(["[1, 2]", "[10, 14]"]))
        