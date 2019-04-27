def BracketMatcher(string):
    matching = []
    
    for x in string:
        if x == "(":
            matching.append(x)
        if x == ")":
            if "(" in matching:
                matching.pop()
            else:
                return 0
    
    
    if len(matching) == 0:
        return 1
    else:
        return 0 


print(BracketMatcher("(hello (world))"))
        
    