def PalindromicSubstring(string):
    addfirst = []
    addlast =  []
    count = 0
    
    strList = list(string)
    
    while len(strList) > 2:
        first = strList.pop(0)
        last = strList.pop()
        
        if first == last:
            count +=1
            
        
        
            
            