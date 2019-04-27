def Division(num1,num2):
    a = 0
    b = 0
    
    if num1 < num2:
        a = num2
        b = num1
    elif num1 > num2:
        a = num1
        b = num2
    
    while a % b != 0:
        r = a % b
        a = b
        b = r
    
    return b 

print(Division(36,54))
    
        
    
    
        
    
     