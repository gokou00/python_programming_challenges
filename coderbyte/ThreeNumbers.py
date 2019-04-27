def ThreeNumbers(string):
    store = ""
    isAdj = False
    count = 0
    strarry = string.split(" ")
    length = len(strarry)
    #print(strarry)
    
    for x in strarry:
        for m in x:
            if m >= "0" and m <= "9":
                temp = x.count(m)
                if temp > 1:
                    return False
    


        
    
    
    for i in range(len(string)):
        if string[i] >= "0" and string[i] <= "9" and i < len(string) -1:
            if string[i+1] >="0" and string[i+1] <= "9":
                if string[i] == string[i+1]:
                    return False
                elif i == len(string) -2:
                    return True
            else:
                count+= 1
        #print(count)
        
        if string[i] == " ":
            print(count)
            if count <= 1:
                return False
            else:
                count = 0
    
    print(count)
    if count <= 1:
        return False
    else:
        return True


    #return True

print(ThreeNumbers("1a2a3 bb34b6 cc7c16c"))
    

        
        