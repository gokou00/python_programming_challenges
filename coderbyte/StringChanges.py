def StringChanges(string):
    buildStr = ""
    strArry = list(string)
    count = 0
    
    while count < len(strArry):
        if strArry[count] == "M" and count-1 >= 0:
            strArry[count] = strArry[count-1]
            #del strArry[count]
            count = 0
            buildStr = ""
            continue
        elif strArry[count] == "M" and count -1 < 0:
            del strArry[count]
            count = 0
            buildStr = ""
            continue
        
        elif strArry[count] == "N" and count + 1 < len(strArry):
            del strArry[count]
            del strArry[count]
            count = 0
            buildStr = ""
        elif strArry[count] == "N" and count + 1 >= len(strArry):
            del strArry[count]
            count  = 0
            buildStr = ""
            continue
        else:
            #buildStr += strArry[count].lower()
            count += 1
            
        
    return "".join(strArry)



print(StringChanges("oMoMkkNrrN"))
        
            
            
            
            
            
            
    