def CaesarCipher(string,num):
    
    finalStr = ""
    
    for x in string:
        if x.isalpha():
            temp = ord(x) + num
            print(temp)
            
            if ord(x) >= 97 and ord(x) <= 122:
            
                if temp > 122:
                    temp1 = temp - 122
                    if temp1 == 1:
                        finalStr += chr(97)
                        continue
                    else:
                        temp2 = 97 + temp1 -1
                        finalStr += chr(temp2)
                #print(temp1)
                        continue
            #elif temp == 122:
                #finalStr += chr(122)
                elif temp >= 97 and temp <= 122:
                    finalStr += chr(temp)
                    continue
            if ord(x) >= 65 and ord(x) <= 90:
            
                if temp > 90:
                
                    temp1 = temp - 90
                    print(temp1)
                    if temp1 == 1:
                        finalStr += chr(65)
                        continue
                    else:
                        temp2 = 65 + temp1 -1
                        finalStr += chr(temp2)
                        continue

                else:
                    print(chr(temp))
                    finalStr += chr(temp)
                    continue
        
        else:
            finalStr += x
    
    
    return finalStr




print(CaesarCipher("byte",13))
                
            