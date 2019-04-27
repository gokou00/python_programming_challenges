def Palindrome(str):
    str = str.replace(" ","")
    return str == str[::-1]
    
    
    

print(Palindrome("never odd or even"))