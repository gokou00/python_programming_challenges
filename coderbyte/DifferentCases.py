def DifferentCases(string):
    cap = False
    stringBuilder = ""
    
    stringBuilder += string[0].upper()
    for x in string[1:]:
        if cap:
            stringBuilder+= x.upper()
            cap = False
            continue
        if x.isalpha() == False:
            cap = True
            continue
        
        stringBuilder += x.lower()
    
    
    return stringBuilder



print(DifferentCases("cats AND*Dogs-are Awesome"))
        