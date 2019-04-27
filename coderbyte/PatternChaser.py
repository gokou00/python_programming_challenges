import re
def PatternChaser(string):
    length = 0
    x = 0
    y = 0
    match = "no null"
    
    for y in range(len(string)):
        for x in range(len(string)):
            substring = string[y:x]
            if len(list(re.finditer(substring,string))) > 1 and len(substring) > length:
                match = substring
                length = len(substring)
                
    if len(match) <= 1:
        return "no null"
    else:
        return "yes "+match
    
    return match
    
    

print(PatternChaser("aabbaa"))
    
    
    
    


    