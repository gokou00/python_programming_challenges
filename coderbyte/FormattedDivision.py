import math
def FormattedDivision(num1,num2):
    total = num1 / float(num2)
    
    frac,whole = math.modf(total)
    stringBuild = ""
    
    #print(total)
    frac = round(frac,4)
    #print(frac)
    #print(whole)
    count = 0
    
    if whole == 0.0 and frac > 0.0:
        decStr = str(frac)
        if len(decStr[2:]) < 4:
            diff = 4 - len(decStr[2:])
            return decStr +  "0" * diff
        else:
            return decStr
    
    
    if whole > 0.0 and frac == 0.0:
        print("test")
        wholeStr = str(whole)
        idx = wholeStr.index(".")
        wholeStr = wholeStr[:idx]
        #wholeStrStack = list(wholeStr)
        revWholeStr = wholeStr[::-1]
        print(wholeStr)
        if len(wholeStr) < 3:
            print("test2")
            return wholeStr + ".0000"
        else:
            for x in revWholeStr:
                if count == 3:
                    stringBuild += ","
                    count = 0
                
                stringBuild += x
                count += 1
    
    
    if stringBuild != "":
        return stringBuild[::-1] + ".0000"
    
    
    
    if whole > 0.0:
        wholeStr = str(whole)
        wholeStr = wholeStr[:-2]
        #print(wholeStr)
        #wholeStrStack = list(wholeStr)
        revWholeStr = wholeStr[::-1]
        #print(revWholeStr)
        if len(wholeStr) < 3:
            stringBuild = wholeStr
        else:
            for x in revWholeStr:
                
                if count == 3:
                    stringBuild += ","
                    #stringBuild += x
                    count = 0
                    #continue
                
                stringBuild += x
                count += 1
                
        
            stringBuild = stringBuild[::-1]
    
    
    if frac > 0.0:
        decStr = str(frac)
        if len(decStr[2:]) < 4:
            diff = 4 - len(decStr[2:])
            decStr =  decStr +  "0" * diff
    
    print(stringBuild)
    print(decStr)    
    
    return stringBuild + decStr[1:]

        
            
            
        
                
        
            
        
        



print(FormattedDivision(101077282 ,21123))