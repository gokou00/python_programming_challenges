def findAndReplacePattern(words, pattern):
    #words2 = ["abc","deq","mee","aqq","dkd","ccc"]
    patternDict = {}
    finalArr = []
    
    #test = list(map(lambda x: str(pattern.count(x)), pattern))
    #print(test,"Pattern")
    count = 0
    for x in pattern:
        if x not in patternDict:
            count += 1
            patternDict[x] = count
        else:
            continue
    
    #print(patternDict)
    
    patterStr = ""
    
    for x in pattern:
        patterStr += str(patternDict[x])
    
    wordDict = {}
        
    count = 0
    for word in words:
        for letter in word:
            if letter not in wordDict:
                count += 1
                wordDict[letter] = count
            else:
                continue
        wordArr = map(lambda x:str(wordDict[x]) ,word)
        #print(wordArr)
        wordPattern = "".join(wordArr)
        if wordPattern == patterStr:
            finalArr.append(word)
            
        wordDict = {}
        count = 0
    
    #print(patterStr)
    #print(finalArr)
    return finalArr
    

    
    
    #return finalArr
        
    
    
    
    
    

print(findAndReplacePattern(["badc","abab","dddd","dede","yyxx"],"baba"))
    

    
    