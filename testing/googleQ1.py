def googleQ(s1,s2):
    strhash = 0
    strhash2 = 0
    strBuild = ""
    
    for x in s1:
        strhash+= hash(x)
    
    for i in range(len(s2)):
        for j in s2[i:i+len(s1)]:
            strBuild += j
            strhash2 += hash(j)
        
        print(strBuild)
        strBuild = ""
        if strhash == strhash2:
            return i
        strhash2 = 0
            
   
    
    return -1
    

print(googleQ("ABCDEF","jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"))
            
            
        