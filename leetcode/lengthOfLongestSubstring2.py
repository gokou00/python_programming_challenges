def lengthOfLongestSubstring(s):
    visted = {}
    count  = 0
    start = 0
    end = 0
    largest = 0
    
    
    for i in range(len(s)):
        if s[i] in visted:
            start = max(start,visted[s[i]]+1)
        
        visted[s[i]] = i
        largest = max(largest, i - start +1)
    
    return largest

            
        
        
        
    #print(temp)
    
    
    #print(end, " end")
    #print(start, "start")
    #temp = end - start
    #temp += 1
    
    #if temp > largest:
        #largest = temp
         
    
    #print(temp)
    #print(visted)
    
    #return largest
        
    
    

print(lengthOfLongestSubstring("abcadcef"))
            
            
        
        
        