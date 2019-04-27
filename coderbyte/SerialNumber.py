def SerialNumber(string):
    
    
    for x in string:
        if x == ".":
            continue
        
        if x >="0" and x <= "9":
            continue
        else:
            return "false"
        
    
    
    stringArr = string.split(".")
    
    if len(stringArr) != 3:
        return "false"
    
    
    group1 = stringArr[0]
    group2 = stringArr[1]
    group3 = stringArr[2]
    
    group1Arr = list(group1)
    group2Arr = list(group2)
    group3Arr = list(group3)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for x in group1Arr:
        sum1 += int(x)
    for x in group2Arr:
        sum2 += int(x)
    for x in group3Arr:
        sum3 += int(x)
    
    
    if sum1 % 2 != 0:
        return "false"
    
    if sum2 % 2 != 1:
        return "false"
    
    if int(group1Arr[-1]) > int(group1Arr[-2]) and int(group1Arr[-1]) > int(group1Arr[-3]) and int(group2Arr[-1]) > int(group2Arr[-2]) and int(group2Arr[-1]) > int(group2Arr[-3]) and int(group3Arr[-1]) > int(group3Arr[-2]) and int(group3Arr[-1]) > int(group3Arr[-3]):
        test = 0
    else:
        return "false"
    
    return "true"
    


print(SerialNumber("114.568.112"))
    
    
    
    
    
    