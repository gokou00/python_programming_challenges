def reflectString(inputString):
    alphabetString = "abcdefghijklmnopqrstuvwxyz"
    revStr = alphabetString[::-1]
    
    alpMap = {}
    
    for i in range(len(alphabetString)):
        alpMap[alphabetString[i]] = revStr[i]
    
    
    finalStr = ""
    
    for x in inputString:
        finalStr += alpMap[x]
    
    return finalStr


print(reflectString("codesignal"))