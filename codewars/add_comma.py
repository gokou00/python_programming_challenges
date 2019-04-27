import math
def commas(num):
    fact,whole = math.modf(num)
    hasFrac = False
    hasNeg = False
    count = 0
    strbuild = ""
    final = ""
    
    if fact != 0.0:
        fact = round(fact,3)
        hasFrac = True
    #print(fact)
    
    if math.fabs(fact) >= 1 :
        #print("wrong")
        whole = fact + whole
        hasFrac = False
    
    strWhole = str(int(whole))
    strFrac = ""
    
    if hasFrac:
        strFrac = str(fact)
    
    if strWhole[0] == "-":
        hasNeg = True
        strWhole = strWhole[1:]
    
    strWhole = strWhole[::-1]
    #print(strWhole)
    
    for x in strWhole:
        if count == 3:
            strbuild += ","
            count = 0
        
        strbuild += x
        count += 1
    
    #print(strbuild)
    
    if hasFrac:
        print(strbuild[::-1])
        print(strFrac)
        if strFrac == "0.0" or strFrac == "-0.0":
             final = strbuild[::-1]
        elif strFrac[0] == "-":    
            final = strbuild[::-1]  + strFrac[2:]
        else:
            final = strbuild[::-1]  + strFrac[1:]
    else:
        final = strbuild[::-1]
        #final = final[:-2]
    
    if hasNeg:
        final = "-" + final
        return final
    else:
        return final
    
        


print(commas(-1000000.123))
    