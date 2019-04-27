def DashInsertII(string):
    stringBuilder = ""
    
    for i in range(len(string)-1):
        if (int(string[i]) % 2 == 0 and int(string[i+1]) % 2 == 0) and (int(string[i]) != 0 and int(string[i+1]) != 0):
            stringBuilder += string[i]
            stringBuilder+= "*"
            #stringBuilder+= string[i+1]
            continue
        
        if (int(string[i]) % 2 != 0 and int(string[i+1]) % 2 != 0) and (int(string[i]) != 0 and int(string[i+1]) != 0):
            stringBuilder += string[i]
            stringBuilder += "-"
            #stringBuilder += string[i+1]
            continue
        
        stringBuilder += string[i]
    
    
    
    stringBuilder += string[-1]
    
    return stringBuilder



print(DashInsertII("4546793"))
            
        