def CamelCase(string):
    finalStr = ""
    toCap = False
    
    if string[0].isalpha():
        finalStr += string[0].lower()
    
    for x in string[1:]:
        if x.isalpha() == False:
            toCap = True
            continue
        if toCap:
            toCap = False
            finalStr += x.upper()
            continue
        finalStr += x.lower()
    
    
    #print(finalStr)
    return finalStr

print(CamelCase("BOB loves-coding"))
            
        
        