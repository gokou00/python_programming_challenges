def TripleDouble(num1,num2):
    num1Str = str(num1)
    num2Str = str(num2)
    
    #digit = ""
    
    for x in num1Str:
        if (num1Str.count(x) >=3) and (num1Str.find(x*3) != -1) and (num2Str.find(x*2) != -1):
            return 1
    
    
    
    #print(num1Str.find("5"*3))
    #print(num2Str.find("5"*2))
    return 0


print(TripleDouble(67844,66237))
            