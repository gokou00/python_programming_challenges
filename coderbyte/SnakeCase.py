def SnakeCase(string):
    finalStr = ""
    for x in string:
        if x.isalpha() == False:
            finalStr += "_"
            continue
        
        finalStr += x.lower()
    
    return finalStr


print(SnakeCase("a b c d-e-f%g"))
    