def reverseWords(s):
    s.strip()
    
    wordList = s.split(" ")
    
    finalStr = ""
    
    print(wordList)
    
    for x in wordList[::-1]:
        if x == "":
            continue
        finalStr+=x
        finalStr+= " "
    
    
    return finalStr[:-1]
    
    
print(reverseWords("the    sky   is   blue"))
    