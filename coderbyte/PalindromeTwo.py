def PalindromeTwo(string):
    strbuild = ""
    
    for x in string:
        if x.isalpha() == False:
            continue
        
        strbuild += x.lower()
    
    return strbuild == strbuild[::-1]