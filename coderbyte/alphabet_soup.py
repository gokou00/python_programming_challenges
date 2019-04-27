def AlphabetSoup(str):
    alpha = list(str)
    print(alpha)
    alpha.sort()
    print(alpha)
    finalStr = "".join(alpha)
    return finalStr
    
    
    
    
    
    
    
    
print(AlphabetSoup("hooplah"))
