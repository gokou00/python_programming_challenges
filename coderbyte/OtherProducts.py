def OtherProducts(arr):
    buildStr = ""
    pro = 1
    finalStr = ""
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            else:
                pro *= arr[j]
        buildStr += str(pro) + "-"
        pro = 1
        
    
    for i in range(len(buildStr)-1):
        finalStr += buildStr[i]
    
    
    return finalStr
    

print(OtherProducts([3,1,2,6]))
            