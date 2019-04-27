def StringReduction(string):
    i = 0
    
    while i < len(string) -1:
        if string[i] == string[i+1]:
            i +=1
            continue
        elif (string[i] == "a" and string[i+1]) == "b" or (string[i] == "b" and string[i+1] == "a"):
            tempStringList = list(string)
            tempStringList[i+1] = "c"
            del tempStringList[i]
            
            string = "".join(tempStringList)
            i = 0
        elif (string[i] == "b" and string[i+1]) == "c" or (string[i] == "c" and string[i+1] == "b"):
            tempStringList = list(string)
            tempStringList[i+1] = "a"
            del tempStringList[i]
            
            string = "".join(tempStringList)
            i = 0
        elif (string[i] == "a" and string[i+1]) == "c" or (string[i] == "c" and string[i+1] == "a"):
            tempStringList = list(string)
            tempStringList[i+1] = "b"
            del tempStringList[i]
            
            string = "".join(tempStringList)
            i = 0
    return len(string)
            



print(StringReduction("bcab"))
        