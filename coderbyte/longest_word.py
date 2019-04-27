def LongestWord(sen):
    
    array = {}
    
    str = ""
    
    array_words = []
    
    senarray = sen.split(" ")
    
    for x in senarray:
        for y in x:
            if not y.isalnum():
                continue
            else:
                str+= y
        array_words.append(str)
        str = ""

    
    print(array_words) 
    
    temp = array_words[0]
    
    for i in range(1, len(array_words)):
        if len(array_words[i]) > len(temp):
            temp = array_words[i]
    
    print(temp)
    
       
    pass
print(LongestWord("Argument goessdasdasdasdasdad here"))