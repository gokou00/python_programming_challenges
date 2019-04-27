def  QuestionsMarks(string):
    total = 0
    startidx = -1
    endidx = -1
    newStr = ""
    
    
    testArry = string.split("???")
    
    print(testArry)
    
    if len(testArry) <=1:
        return "false"
    
    newStr = "".join(testArry)
    print(newStr)
    
    numStack = []
    isvalid = False
    
    count = 0
    
    for x in string:
        if x >= "0" and x <="9":
            count += 1
    
    
    if count < 2:
        return "false"
    
    
    
    
    for x in newStr:
        if x >= "0" and x <= "9":
            numStack.append(int(x))
            
        if len(numStack) == 2:
            startidx = newStr.index(str(numStack[0]))
            endidx = newStr.index(str(numStack[1]))
            print(numStack)
            
            temp = newStr[startidx:endidx].count("?")
            
            
            if temp > 0:
                numStack = []
            else:
                total = sum(numStack)
                numStack = []
                if total != 10:
                    return "false"
    
        
                    
            
            
            
            
            
        
        

    
    
    
    return "true"
        
    
    
    
    
 
        

            
    
    
    #return "false"
    


print(QuestionsMarks( "arrb6???4xxbl5???eee5"  ))