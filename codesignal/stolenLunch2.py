def stolenLunch(note):
    alpha = "abcdefghij"
    num = "0123456789"
    final = ""
    
    alphaMap = {}
    numMap = {}
    
    for i in range(len(alpha)):
        alphaMap[alpha[i]] = num[i]
        numMap[num[i]] = alpha[i]
    
    
    for x in note:
        if x >= "a" and x <= "j":
            final += alphaMap[x]
        elif x >= "0" and x < "9":
            final += numMap[x]
        else:
            final += x
    
    
    return final


print(stolenLunch("you'll n4v4r 6u4ss 8t: cdja"))
        
    
    
    
    