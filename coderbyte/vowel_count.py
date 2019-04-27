def VowelCount(str):
    vowels = "aeiou"
    
    newStr = str.lower()
    
    count = 0
    
    for x in newStr:
        if x in vowels:
            count +=1
    # code goes here 
    return count
    
print(VowelCount("coderbyte"))