def SimpleSymbols(str):
    isSimple = True
    
    
    if str[0].isalpha() or str[len(str) - 1].isalpha():
        return False
    
    for i in range(len(str)):
        print(i)
        if str[i].isalpha():
            print(str[i])
            if str[i-1] != "+" or str[i + 1] != "+":
                print("test")
                return False
            

    # code goes here 
    return isSimple
    

print(SimpleSymbols("+f+d+=+s+"))
    
    