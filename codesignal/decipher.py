def decipher(cipher):
    finalStr = ""
    
    strBuild = cipher[0:0+3]
    
    inc = 0
    
    while cipher:
        
        numStr = int(strBuild)
        if (numStr >= 65 and numStr <= 90) or (numStr >= 97 and numStr <= 122):
            inc = 3
            finalStr += chr(numStr)
        else:
            inc = 2
            strBuild = cipher[0:0+inc]
            numStr = int(strBuild)
            finalStr += chr(numStr)
        
        tempList = list(cipher)
        tempList = tempList[inc:]
        cipher = "".join(tempList)
        strBuild = cipher[0:0+3]
        
        
            
        #print(chr(int(strBuild)))
    
    return(finalStr)    






print(decipher("98"))