def NumberStream(string):
    
    for x in string:
        num = int(x)
        
        stringbuild = x * num
        #print(stringbuild)
        
        if string.find(stringbuild) != -1:
            return "true"
            
    
    
    return "false"

    


print(NumberStream( "999999999999999992222"))