import operator
def top_3_words(text):
    newText = ""
    wordDict = {}
    finalArr = []
    
    for x in text:
        if x.isalnum() != True and x != " " and x != "'":
            continue
        else:
            newText += x.lower()
    
    
    print(newText)
    
    wordArr = newText.split(" ")
    
    print(wordArr)
    
    for x in wordArr:
        if x == " " or x == "":
            continue
        else:
            if x not in wordDict:
                wordDict[x] = 1
            else:
                wordDict[x] += 1
    
    print(wordDict)
    
    #if a tie the choose the any of the next
    #need to fix the sorting. 
    
    #sorted_x = sorted(wordDict.items(), key=operator.itemgetter(0), reverse=True)
    #print(sorted_x)
    
    sortedValue = sorted(wordDict.values(), reverse = True)
    sortedValue = sortedValue[:3]
    #print(sortedValue)
    
    #for key,value in wordDict.items():
        #if value in sortedValue:
            #finalArr.append(key)
    
    switchDict = {}
    
    for key,value in wordDict.items():
        switchDict[value] = key
    
    
    
    print(switchDict)       
    #print(finalArr)
    
    for x in sortedValue:
        finalArr.append(switchDict[x])
    
    print(finalArr)
    
    if x
    
    
    



print(top_3_words("  '  " ))