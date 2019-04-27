import itertools
def PalindromeCreator(string):
    stringArry = list(string)
    revStringArry = list(string[::-1])
    #print(revStringArry)
    arr_String =[]
    
    if string == string[::-1]:
        return "palindrome"
    
    removedletters = ""
    count = 0
    
    for L in range(0, len(revStringArry)+1):
        for subset in itertools.combinations(revStringArry, L):
            #print(subset)
            rev_temp = "".join(subset)
            #print(rev_temp)
            temp = "".join(subset[::-1])
            #print(temp)
            if rev_temp == temp:
                #print("hit")
                arr_String.append(temp)
                
            
    

    for i in range(len(arr_String)):
        if len(arr_String[i]) < (len(string) - 2):
            arr_String[i] = None
    
    new_arr = []
    
    for x in arr_String:
        if x != None:
            new_arr.append(x)
    
    
    
    
    
    #print(new_arr)
    if len(new_arr) == 0:
        return "not possible"
    
    #found = new_arr.pop()
    
    final_ans = ""
    another_arr =[]
    
    for x in new_arr:
        for n in string:
            if n in x:
                continue
            else:
                final_ans += n
        
        another_arr.append(final_ans)
        final_ans = ""

    

    
    
    if final_ans != "":
        another_arr.append(final_ans)
    isEqual = True
        
    for i in range(len(another_arr) -1):
        if len(another_arr[i]) == len(another_arr[i+1]):
            continue
        else:
            isEqual = False
    
    if isEqual:
        return another_arr[0]
    
    else:
        return another_arr[-1]
            
    
    #return another_arr
    
    
    

print(PalindromeCreator("kjjjhjjj"))
    
    