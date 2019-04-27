def beautifulText(inputString, l, r):
    start = 0
    end = 0
    count = 1
    beautiful = True
    print(len(inputString))
    for i in range(l,r+1):
        end = end + i
        #start =  i + 1
        #print(inputString[start:end] , "Slice")
        #print(inputString[i],"char")
        if (inputString[i-1] != " ") or (len(inputString[start:end]) < l or len(inputString[start:end]) > r):
            start = start + i +1
            continue
        
        for j in range(i+1,len(inputString),i):
            
            if inputString[j] != " " :
                beautiful = False
                break

        if beautiful:
            return True
       

    
    
    if beautiful:
        return True
    else:
        return False



print(beautifulText("Look at this example of a correct text",5,15))
    
    
    