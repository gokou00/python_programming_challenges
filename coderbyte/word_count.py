def WordCount(str):
    strbuild = ""
    strArrary = []
    for x in str:
        if x >= "a" and x <= "z" or x >= "A" and x <= "Z" or x >="1" and x <="9":
            strbuild += x
        else:
            strArrary.append(strbuild)
            strbuild = ""
    
    
    if strbuild != "":
        strArrary.append(strbuild)
        
    return len(strArrary)
    
print(WordCount("All sd 33 dd"))
    