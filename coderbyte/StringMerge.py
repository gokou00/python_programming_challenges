def StringMerge(string):
    stringArr = string.split("*")
    arr1 = stringArr[0]
    arr2 = stringArr[1]
    strBuild = ""
    
    for i in range(len(arr1)):
        strBuild+= arr1[i]
        strBuild+= arr2[i]
    
    
    return strBuild



print(StringMerge("123hg*aaabb"))
        