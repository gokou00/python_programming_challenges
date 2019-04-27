def SwapCase(string):
    buildStr = ""
    for x in string:
        if x >= "a" and x <= "z":
            temp = x.upper()
            buildStr += temp
        elif x >="A" and x <="Z":
            temp = x.lower()
            buildStr += temp
        else:
            buildStr += x
    
    return buildStr
    

print(SwapCase("Hello World"))
    