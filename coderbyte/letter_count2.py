def LetterCountI(str):
    test = {}
    temp = 0
    str_array = str.split(" ")
    count = 0
    for word in str_array:
        test[word] = 0
        for letter in word:
            if word.count(letter) >= 2 and word.count(letter) > temp :
                test[word] = word.count(letter)
                temp = word.count(letter)
                count = temp
    
        temp = 0
    
    isMultiple = False
        
    if len(str_array) == 1:
        for x in str:
            if str.count(x) >= 2:
                isMultiple = True
    
    
    if len(str_array) == 1 and isMultiple:
        return str_array[0]
    elif len(str_array) == 1 and not isMultiple:
        return -1
    
    if count == 0:
        return -1
    
    #print(test)
    
    temp = 0
    answer = str_array[1]
    
    for key,value in test.items():
        if value > temp:
            #print("test")
            answer = key
            temp = value
        elif value == temp:
            if str_array.index(answer) < str_array.index(key):
                continue
            else:
                answer = key
    
    return answer
    
    
    
print(LetterCountI("a b c d ee"))
    