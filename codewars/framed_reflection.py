def mirror(text):
    word_array = text.split(" ")
    largest_word_length = 0
    
    largest_word_length = len(word_array[0])
    
    for x in word_array:
        if len(x) > largest_word_length:
            largest_word_length = len(x)
            
            
    print(largest_word_length)
    
    largest_word_length += 4
    final_string = ""
    
    for i in range(0,largest_word_length):
        final_string += "*"
        
    final_string += "\n"
    
    temp = ""
    
    for x in word_array:
        temp = "* " + x[::-1]
        if len(temp) == largest_word_length - 2:
            final_string += temp + " *\n"
        else:
            for i in range(len(temp),largest_word_length-2):
                temp += " "
            temp += " *\n"
            final_string += temp 
        #final_string += "* " + x[::-1] + " *\n"
        
    for i in range(0,largest_word_length):
        final_string += "*"
    
    print(final_string)
    


mirror("ve mhm fsdz mxbhic tdghdole")
    
    