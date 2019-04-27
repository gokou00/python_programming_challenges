def title_case(title, minor_words = ""):
    if len(title) == 0:
        return ""
    #if len(minor_words) == 0:
     #   return title
    final_Str = ""
    str_Array = []
    title = title.lower()
    minor_words = minor_words.lower()
    first_word = ""
    str_Array = title.split(" ")
    first_word = str_Array.pop(0)
    first_word = first_word.capitalize()
    print(first_word + " first str")
    print(str_Array)
    #cap_array = [x.capitalize() for x in str_Array if x not in minor_words]
    for x in str_Array:
        if x not in minor_words:
            final_Str += x.capitalize() + " "
        else:
            final_Str += x + " "
    print(first_word +" " + final_Str)
    #return first_word + " " + " ".cap_array(cap_array)
    
title_case("the quick brown fox")
    
