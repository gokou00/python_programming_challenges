def ArrayCouples(arr):
    arrStr= ""
    strArr = []
    finalStr = ""
    
    
    for x in arr:
        arrStr += str(x)
    
    #for x in arr:
    
    #if (len(arr) / 2) % 2 == 1:
        
    
    
    for i in range(0,len(arr)-1,2):
        temp = str(arr[i+1]) + str(arr[i])
        
        if str(arr[i+1]) == str(arr[i]):
            if arrStr.count(temp) > 1:
                continue
            else:
                finalStr += str(arr[i]) + "," + str(arr[i+1]) + ","
                continue
        
        if arrStr.find(temp) != -1:
            continue
        else:
            finalStr += str(arr[i]) + "," + str(arr[i+1]) + ","
        
        #print(i)
       
        #print(temp)
        continue
    
    
    
    if finalStr == "":
        return "yes"
    else:
        return finalStr[:-1]



print(ArrayCouples([1,2,3,4,5,6,6,5,4,3,2,10]))
    
    
    