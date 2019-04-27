def WordSplit(strArr):
    word = strArr[0]
    
    stringWords = strArr[1]
    
    arrWords = stringWords.split(",")
    
    for i in range(len(word)):
        
        word1 = word[:i]
        word2 = word[i:]
        
        if word1 in arrWords and word2 in arrWords:
            return word1+  "," + word2
    
    return "not possible"
    
    

print(WordSplit([ "abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz" ]))
        
        