def stolenLunch(note):
    num = "0123456789"
    stringtest = "abcdefghij"
    
    alphaMap = {}
    numMap = {}
    
    for i,x in enumerate(stringtest):
        alphaMap[x] = str(i)
        numMap[str(i)] = x
    
    
    finalStr = ""
    
    for x in note:
        if x >= "0" and x <= "9":
            finalStr += numMap[x]
        elif x >= "a" and x <= "j":
            finalStr += alphaMap[x]
        else:
            finalStr += x
    
    
    return finalStr




print(stolenLunch(""))
        

    
 