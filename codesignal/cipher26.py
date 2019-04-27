def cipher26(message):
    #revMess = message
    finalStr = ""
    sub = 0
    prev = 0 
    
    for x in message:
        t = ord(x) - 97
        sub = t - prev
        
        if(sub < 0):
            sub = sub + 26
        
        finalStr += chr(sub+97)
        
        prev = t
    

    
    
    
    return finalStr
    


print(cipher26("taiaiaertkixquxjnfxxdh"))
    
    
        
    