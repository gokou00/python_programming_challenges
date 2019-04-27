def NoughtsDeterminer(strArr):
    tempStrArr = []
    
    #stringArr = "".join(strArr)
    #print(stringArr[5])
    stringArr = strArr[:]
    
    
    while stringArr.index("-") != -1:
        tempStrArr = strArr[:]
        idx = stringArr.index("-")
        #print(idx)
        #test for X rows
        tempStrArr[idx] = "X"
        if tempStrArr[0] == "X" and tempStrArr[1] == "X" and tempStrArr[2] == "X":
            return idx
        if tempStrArr[4] == "X" and tempStrArr[5] == "X" and tempStrArr[6] == "X":
            return idx
        if tempStrArr[8] == "X" and tempStrArr[9] == "X" and tempStrArr[10] == "X":
            return idx
        
        # test for X cols
        
        if tempStrArr[0] == "X" and tempStrArr[4] == "X" and tempStrArr[8] == "X":
            return idx
        
        if tempStrArr[1] == "X" and tempStrArr[5] == "X" and tempStrArr[9] == "X":
            return idx
            
        if tempStrArr[2] == "X" and tempStrArr[6] == "X" and tempStrArr[10] == "X":
            return idx
        
        #test for diags X
        
        if tempStrArr[0] == "X" and tempStrArr[5] == "X" and tempStrArr[10] == "X":
            return idx
        if tempStrArr[2] == "X" and tempStrArr[5] == "X" and tempStrArr[8] == "X":
            return idx
        
        
        #tempStrArr = strArr[:]
        #idx = stringArr.index("-")
        tempStrArr[idx] = "O"
        
        #test for O's rows
        if tempStrArr[0] == "O" and tempStrArr[1] == "O" and tempStrArr[2] == "O":
            return idx
        if tempStrArr[4] == "O" and tempStrArr[5] == "O" and tempStrArr[6] == "O":
            return idx
        if tempStrArr[8] == "O" and tempStrArr[9] == "O" and tempStrArr[10] == "O":
            return idx
        
        # test for O cols
        
        if tempStrArr[0] == "O" and tempStrArr[4] == "O" and tempStrArr[8] == "O":
            return idx
        
        if tempStrArr[1] == "O" and tempStrArr[5] == "O" and tempStrArr[9] == "O":
            return idx
            
        if tempStrArr[2] == "O" and tempStrArr[6] == "O" and tempStrArr[10] == "O":
            return idx
        
        #test for diags O
        
        if tempStrArr[0] == "O" and tempStrArr[5] == "O" and tempStrArr[10] == "O":
            return idx
        if tempStrArr[2] == "O" and tempStrArr[5] == "O" and tempStrArr[8] == "O":
            return idx
        
        
        tempStrArr[idx] = "S"
        #stringArr = "".join(tempStrArr)
        #stringArr = tempStrArr[:]
        stringArr[idx] = "S"
        #print(stringArr)

print(NoughtsDeterminer( ["X","O","-","<>","-","O","-","<>","O","X","-"]))
        
        
        
        
        
        
            