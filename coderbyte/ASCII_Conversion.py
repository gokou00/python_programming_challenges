def ASCIIConversion(string):
    finalStr = ""
    
    for x in string:
        if x == " ":
            finalStr += " "
            continue
        
        finalStr += str(ord(x))
    
    
    #print(finalStr)
    return finalStr


print(ASCIIConversion("abc **"))
    