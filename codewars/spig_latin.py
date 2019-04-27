def pig_it(text):
    #your code here
    ending = "ay"
    text_array = text.split(" ")
    final_array = []
    
    for x in text_array:
        if x.isalnum():
            final_array.append(x[1:] + ending)
        else:
            final_array.append(x)
    
    return " ".join(final_array)
    
    
print(pig_it('a'))
    
    