def integerToStringOfFixedWidth(number, width):
    numStr = ""
    
    while number != 0 and len(numStr) != width:
        pop = number % 10
        numStr += str(pop)
        number /= 10
        
        
    if len(numStr) < width:
        while len(numStr) < width:
            numStr += str(0)
            
    
    return numStr[::-1]
    


print(integerToStringOfFixedWidth(0,1))