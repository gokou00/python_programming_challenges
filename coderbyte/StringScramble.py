def StringScramble(str1,str2):
    for x in str2:
        if x not in str1:
            return "false"
    
    return "true"
    

print(StringScramble("h3llko","hello"))