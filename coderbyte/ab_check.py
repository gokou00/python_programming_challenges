def ABCheck(str):
    newstr = str.lower()
    first_a = newstr.rfind("a")
    first_b = newstr.rfind("b")
    
    print(first_a , first_b)
    
    if first_a > first_b:
        length = (first_a - 1) - (first_b - 1)
        length -= 1
        
    if first_a < first_b:
        length = (first_b - 1) - (first_a - 1)
        length -= 1
        
    
    if length == 3:
        return True
    else:
        return False    

    # code goes here 
    return str
    
    
print(ABCheck("bzzza"))

    