def RemoveBrackets(string):
    stackstring = []
    arrString = list(string)
    
    for x in string:
        if x == "(":
            stackstring.append(x)
        elif x == ")":
            if "(" not in stackstring:
                stackstring.append(x)
            elif "(" in stackstring:
                stackstring.pop()
    
    
    return len(stackstring)


print(RemoveBrackets("(()("))
    
    
    