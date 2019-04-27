def PalindromeSwapper(string):
    revString = string[::-1]
    count = 0
    
    if string == revString:
        return string
    
    #for i in range(len(string)):
        #if string[i] != revString[i]:
            #count += 1
    
    
    #if count > 2:
        #return "First fail"
    
    
    for i in range(len(string)):
        if string[i] != revString[i]:
            swap = string[i]
            temp = list(string)
            temp2 = list(string)
            if i == 0:
                temp[i] = temp[i+1]
                temp[i+1] = swap
                string = "".join(temp)
                if string == string[::-1]:
                    return string[::-1]
                else:
                    return -1
            
            if i == len(string)-1:
                temp[i] = temp[i-1]
                temp[i-1] = swap
                string = "".join(temp)
                if string == string[::-1]:
                    return string[::-1]
                else:
                    return -1
            
            else:
                temp[i] = temp[i-1]
                temp[i-1] = swap
                string = "".join(temp)
                if string == string[::-1]:
                    return string[::-1]
                
                
                temp2[i] = temp2[i+1]
                temp2[i+1] = swap
                string = "".join(temp2)
                if string == string[::-1]:
                    return string[::-1]
                    
    
    
    return -1


print(PalindromeSwapper("kyaak"))
                
            