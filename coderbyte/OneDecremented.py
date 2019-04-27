def OneDecremented(num):
    numStr = str(num)
    
    numStrArry = list(numStr)
    count = 0
    
    for i in range(len(numStrArry)-1):
        if int(numStrArry[i]) > int(numStrArry[i+1]) and int(numStrArry[i]) - int(numStrArry[i+1]) == 1  :
            count += 1
        
    
    
    return count


print(OneDecremented(9876541110))