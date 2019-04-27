def ArrayMatching(strArr):
    str1 = strArr[0]
    str2 = strArr[1]
    str1Stripped = ""
    str2Stripped = ""
    finalStr = ""
    final = ""

    for x in str1:
        if x == "[" or x == "]":
            continue
        
        str1Stripped += x
    
    for x in str2:
        if x == "[" or x == "]":
            continue
        
        str2Stripped += x
    
    
    
    
    array1 = str1Stripped.split(",")
    array2 = str2Stripped.split(",")
    
    #print(array1)
    #print(array2)
    
    if len(array1) == len(array2):
        for i in range(len(array1)):
            finalStr += str(int(array1[i]) + int(array2[i]))
            finalStr += "-"
    
    if len(array1) > len(array2):
        count = 0
        while count < len(array2):
            finalStr += str(int(array1[count]) + int(array2[count]))
            finalStr += "-"
            count += 1
        
        while count < len(array1):
            finalStr+= array1[count]
            finalStr += "-"
            count +=1
    
    if len(array2) > len(array1):
        count = 0
        while count < len(array1):
            finalStr += str(int(array2[count]) + int(array1[count]))
            finalStr += "-"
            count += 1
        
        while count < len(array2):
            finalStr+= array2[count]
            finalStr += "-"
            count +=1
            
    for x in finalStr:
        if x != " ":
            final += x
            

    #print(final)        
    
    final = final[:-1]
        
        
        
    
    #print(final)
    return final

print(ArrayMatching(["[1, 2, 1]", "[2, 1, 5, 2]"]))