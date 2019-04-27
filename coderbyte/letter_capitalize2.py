def LetterCapitalize(str):
    

    words = str.split(" ")
    print(words)
    
    final = ""
    count = 0
    
    for x in words:
        for y in x:
            if count == 0:
                cap = y.capitalize()
                final += cap
                count += 1
            else:
                final += y
        
        count = 0
        final += " "
    
    
    print(final)
    
    
    
     
    pass



LetterCapitalize("h3llo yo people")
    
    
