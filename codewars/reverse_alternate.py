def reverse_alternate(string):
    strArry = []
    strbuild = ""
    
    if string == "":
        return ""
    elif string == " ":
        return " "
    
    
    for x in string:
        if x == " ":
            strArry.append(strbuild)
            strbuild = ""
        else:
            strbuild += x
    
    if strbuild != "":
        strArry.append(strbuild)
        
    
    for i in range(1,len(strArry)):
        if (i + 1) % 2 == 0:
            strArry[i] = strArry[i][::-1]
        else:
            continue
        
        
    
    
    
    
    
    print(strArry)
    
    final = " ".join(strArry)
    print(final)
    
    
    
    
    
    

print(reverse_alternate("I really hope it works this time..."))
  