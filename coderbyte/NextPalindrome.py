def NextPalindrome(num):
    found = False
    ans = ""
    
    while not found:
        num+= 1
        temp = str(num)
        if temp == temp[::-1]:
            found = True
            ans = temp[::-1]
        
    
    return int(ans)

print(NextPalindrome(24))
        