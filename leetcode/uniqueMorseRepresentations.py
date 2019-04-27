def uniqueMorseRepresentations(words):
    morseCode =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    morseDict = {}
    for i in range(len(morseCode)):
        morseDict[alpha[i]] = morseCode[i]
    
    
    wordsMorse = []
    temp = ""
    
    for x in words:
        for k in x:
            temp += morseDict[k]
        
        wordsMorse.append(temp)
        temp = ""
        
    
    return len(set(wordsMorse))
    


print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
        