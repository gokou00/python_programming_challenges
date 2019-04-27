def NonrepeatingCharacter(string):
    
    for x in string:
        if string.count(x) == 1 and x != " ":
            return x
            
    
    return "Can't find"


print(NonrepeatingCharacter("hello world hi hey"))