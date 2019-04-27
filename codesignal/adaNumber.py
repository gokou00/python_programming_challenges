def adaNumber(line):
    num = {}
    numbers = "0123456789abcdef"
    for i in range(2,17):
        temp1 = str(i)
        num[temp1] = ""
        for j in range(0,i):
            num[temp1] += numbers[j]
    
    
    line = line.strip()
    
    newline = ""
    for x in line:
        if x == "_":
            continue
        else:
            newline += x
    
    line = newline
    #print(line)
    
    
    idx = line.find("#")
    
    test2 = ""
    
    if idx == -1:
        for x in line:
            if x == "_":
                continue
            elif x not in num["10"]:
                return False
            elif x in num["10"]:
                test2 += x
        if len(test2) != 0:
            return True
        else:
            return False
        
    
    
    
    
    
    base = line[:idx]
    
    
    if base not in num:
        print("failed here")
        return False
    
    while idx < len(line):
        #idx = line.find("#")
        newidx = 0
        test = ""
        for i in range(idx+1,len(line)):
            if line[i] == "_":
                continue
            elif line[i] == "#":
                newidx = i
                break
            elif line[i].lower() not in num[base]:
                return False
        
            elif line[i].lower() in num[base]:
                test += line[i].lower()
                
        if newidx == len(line) -1:
            break
        else:
            oldidx = idx
            idx = newidx
            base = line[oldidx+1:idx]
            if base not in num:
                return False
    
    
    #print(test)
    if len(test) != 0:
        return True
    else:
        return False
    
    
    
                
        
        
        
        
    



print(adaNumber("__" ))