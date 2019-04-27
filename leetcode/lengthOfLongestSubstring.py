def lengthOfLongestSubstring(s):
    #subStringArr = []
    strBuild = ""
    largest = 0
    largestStr = ""
    count = 0
    stack = []
    lengthArr = []
    
    while count < len(s):
        if s[count] not in stack:
            #strBuild += s[count]
            stack.append(s[count])
            count += 1
        else:
            if s[count] == s[count -1]:
                
                lengthArr.append(len(stack))
                
                stack = []
                stack.append(s[count])
                
                count +=1
                continue
            else:
                #count -= 1
                lengthArr.append(len(stack))
                idx = s[:count].rindex(s[count])
                #print(s[idx])
                count = idx + 1
                stack = []
                stack.append(s[count])
                #largest = len(strBuild)
                #largestStr = strBuild
                #strBuild = s[count]
                count+= 1
        print(stack)
    
    lengthArr.append(len(stack))
    
    #print(stack)
    #print(lengthArr)
    
    lengthArr.sort()
    
    
    
    return lengthArr[-1]
    
    #return len(strBuild)



print(lengthOfLongestSubstring(  "anviaj"  ))
                
            
            