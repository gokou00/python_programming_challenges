def BitwiseTwo(strArr):
    finalStr = ""
    string1 = strArr[0]
    string2 = strArr[1]
    
    for i in range(len(string1)):
        if string1[i] == "1" and string2[i] == "1":
            finalStr += "1"
        else:
            finalStr += "0"
    
    return finalStr
    
print(BitwiseTwo(["10100", "11100"]))