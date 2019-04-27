def LetterChanges(str):
    newStr = ""
    letters = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZaeiouAEIOU"
    
    finalStr = ""
    
    for x in str:
        if x == "z":
            x = "A"
            newStr += x
            continue
            
        if x == "Z":
            x = "A"
            newStr += x
            continue
            
            
        if x in letters:
            tempNum = ord(x)
            tempNum += 1
            if chr(tempNum) in "aeiou" or chr(tempNum) in "AEIOU":
                newStr += chr(tempNum).capitalize()
            else:
                newStr += chr(tempNum)
        else:
            newStr += x
        
        
        
    
    
    print(newStr)
    
LetterChanges("fun times!")
    

    