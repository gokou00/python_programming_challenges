def theSmallestStringCipher(key, message):
    finalStr = ""
    finalStr2 = ""
    keyList = list(key)
    messageList = list(message)
    keyidx = 0
    messageidx = 0
    #print(keyList)
    #print(messageList)
    count = 0 
    
    while keyidx < len(keyList) and messageidx < len(messageList):
        #print(keyList[keyidx], " key")
        #print(messageList[messageidx], " message")
        if keyList[keyidx] < messageList[messageidx]:
            finalStr += keyList[keyidx]
            finalStr2 += keyList[keyidx]
            keyidx+=1
        elif keyList[keyidx] == messageList[messageidx]:
            temp1 = ""
            temp2 = ""
            temp1 += key[keyidx:] + message[messageidx:]
            temp2 += message[messageidx:] + key[keyidx:]
            
            if temp1 < temp2:
                finalStr += keyList[keyidx]
                keyidx += 1
            else:
                finalStr += messageList[messageidx]
                messageidx+=1

        else:
            finalStr += messageList[messageidx]
            finalStr2 += messageList[messageidx]
            messageidx += 1
        #print(finalStr, "finalStr")

    
    #print(keyidx)
    #print(messageidx)
    #print(finalStr)
    #print(messageList[messageidx:])
    
    if keyidx == len(keyList):
        finalStr += message[messageidx-count:]
        finalStr2 += message[messageidx:]
    else:
        print("test")
        finalStr += key[keyidx-count:]
        finalStr2 += key[keyidx-count:]
        
    print(finalStr , "finalStr")
    print(finalStr2, "finalStr2")
    
    return finalStr
    


print(theSmallestStringCipher("ggzhotybqcjwbekrxlgs" ,"lneevzpnpbtptiraomss" ))
        