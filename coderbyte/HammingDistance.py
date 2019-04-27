def HammingDistance(strArr):
    count = 0
    str1 = strArr[0]
    str2 = strArr[1]
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count +=1
            
    
    return count
    
    

print(HammingDistance(["helloworld", "worldhello"]))