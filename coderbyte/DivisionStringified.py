def DivisionStringified(num1,num2):
    ans = round(num1 / float(num2))
    print(int(ans))
    
    ans = int(ans)
    strAns = str(ans)
    
    if len(strAns) <= 3:
        return strAns
    
    revStr = strAns[::-1]
    strbuild = ""
    
    for i in range(0,len(revStr)):
        if i % 3 == 0 and i != 0:
            strbuild+=","
        
        strbuild+= revStr[i]
    
    
    print(strbuild[::-1])
            
        

DivisionStringified(63,14)
    