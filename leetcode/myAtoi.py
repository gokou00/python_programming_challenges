def myAtoi(string):
    INT_MAX = (2 ** 31) -1
    INT_MIN = -2**31
     
    #print(INT_MIN)
    #print(INT_MAX)
    
    numStr = ""
    
    string = string.lstrip(" ")
    numArr = ["0","1","2","3","4","5","6","7","8","9"]
    
    if string[0] == "+" or string[0] == "-" or (string[0] >= "0" and string[0] <= "9"):
        numStr += string[0]
    
        for i in range(1,len(string)):
            #print(string[i])
            if string[i] not in numArr:
                print("test")
                break
            numStr += string[i]
    
        #print(int("-232323"))
        
        print(numStr)
        
        try:
            convert = int(float(numStr))
        except:
            #print("not an int")
            return 0 
            
    
        
        
        
    else:
        return 0 
     
    if convert < INT_MIN:
         return INT_MIN
    elif convert > INT_MAX:
        return INT_MAX
    
    return convert    
     
     
     
     

print(myAtoi( " -88827 5655 U"  ))