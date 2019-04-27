def longestValidParentheses(s):
    count = 0
    arr = []
    
    
    if s.find("()") == -1:
        return 0
    
    idx = s.find("()")
    count = 2
    
    idx = idx +2
    newWord = s[idx:]
    arr.append(count)
    
    for x in newWord:
        idx = newWord.find("()")
        #print(idx)
        #print(newWord)
        
        if idx == 0:
            count += 2
            idx = idx + 2
            newWord = newWord[idx:]
            
        elif idx == -1:
            arr.append(count)
            break
        else:
            print("test")
            arr.append(count)
            count = 2
            idx = idx + 2
            newWord = newWord[idx:]
        
        
        
    #if count != 
    
    arr.sort()
    #print(arr[-1])
    return arr[-1]



print(longestValidParentheses( "()(())"  ))