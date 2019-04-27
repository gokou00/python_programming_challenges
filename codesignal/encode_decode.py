def encodingDecoding(message):
    base_encode = 0
    count = 0
    final_str = ""
    numhex = []
    hexcount = 0
    buildhex = ""
    if message == "":
        return ""
    if message[0] >= "0" and message[0] <="9":
        for x in message:
            if hexcount == 2:
                numhex.append(buildhex)
                buildhex = x
                hexcount = 1
            else:
                buildhex += x
                hexcount +=1
        
        if buildhex != "":
            numhex.append(buildhex)
        
        #print(numhex)
        print(chr(int(numhex[2], 16) -2))
        
        for x in numhex:
            print(x)
            if count == 0:
                final_str += chr(int(x, 16))
                count += 1
            else:
                final_str += chr(int(x, 16) - count)
                count +=1
        print(final_str)
                
        
        return
    
            
        
    diff = 0
    
    for x in message:
        if (x >= "a" and x <= "z" and count == 0) or (x >= "A" and x <= "Z" and count == 0):
            #print("test1")
            base_encode = format(ord(x), "x")
            base = format(ord(x), "x")
            final_str += str(format(ord(x), "x"))
        elif x >= "a" and x <= "z" or x >= "A" and x <= "Z":
            #print("test2")
            
            base_encode = format(ord(x), "x")
            diff = str(int(base,16) - int(base_encode,16))
            
            ans = int(base_encode,16) - int(diff,16)
             
            final_str += str(ans)
            
        count+=1
    
    print(final_str)
    print(count)
            
            
            
            
            
encodingDecoding("Hi")