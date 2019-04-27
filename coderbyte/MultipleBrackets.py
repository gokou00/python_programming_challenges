def MultipleBrackets(string):
    stackofBrackets = []
    count = 0
    
    if (string.count("(") == 0 and string.count(")") == 0) or (string.count("[") == 0 and string.count("]") == 0):
        return 1
        
    
    for x in string:
        if x == "(" or x== "[":
            #print(x)
            stackofBrackets.append(x)
        if x == ")":
            if "(" in stackofBrackets:
                idx = stackofBrackets.index("(")
                del stackofBrackets[idx]
                count += 1
            else:
                #print("failed ) ")
                return 0 
        elif x == "]":
            if "[" in stackofBrackets:
                idx = stackofBrackets.index("[")
                del stackofBrackets[idx]
                count += 1
            else:
                #print("failed ]")
                return 0
        #print(stackofBrackets)
    
    #print(stackofBrackets)
    if len(stackofBrackets) == 0:
        return str(1) +" "+ str(count)
    else:
        return 0 
        
    
    


print(MultipleBrackets(  "one(bracket)"  ))
            