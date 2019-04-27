def NumberSearch(string):
    numArr = []
    count = 0
    
    for x in string:
        if x.isdigit():
            numArr.append(int(x))
            #count +=1
        if x.isalpha():
            count+= 1
    
    
    arrSum = sum(numArr)
    #print(arrSum)
    #print(count)
    
    #print( round(arrSum/float(count)) )
    
    return int(round(arrSum/float(count)))
    


print(NumberSearch("Hello6 9World 2, Nic8e D7ay!"))