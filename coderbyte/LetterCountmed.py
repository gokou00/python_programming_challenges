def LetterCount(string):
    largest = 0
    largestWord = ""
    stringArr = string.split(" ")
    
    
    for word in stringArr:
        #print(word)
        for letter in word:
            #print(letter)
            if word.count(letter) > 1 and word.count(letter) > largest:
                largest = word.count(letter)
                largestWord = word
    
    
    
    if largestWord == "":
        return -1
    else:
        return largestWord
    
    


print(LetterCount("No words"))
    