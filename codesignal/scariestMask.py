def scariestMask(mask):
    revStr = ""
    count = 0
    final_count = 0
    
    for x in mask:
        revStr = x[::-1]
        for j in x:
            if j != revStr[count]:
                final_count += 1
            
            count+=1
        
        count = 0
    
    
    print(final_count)
    
    print(final_count/2)
    
    
scariestMask(["@"])
        
        
        
                