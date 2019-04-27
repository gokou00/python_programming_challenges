def PowersofTwo(num):
    powerOfTwoArray =[]
    
    for i in range(1,100):
        temp = 2 ** i
        powerOfTwoArray.append(temp)
        
        
    if num in powerOfTwoArray:
        return True
    else:
        return False
    
    print(powerOfTwoArray)
    
    

PowersofTwo(8)


