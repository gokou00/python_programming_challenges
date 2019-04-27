import itertools
def CountingAnagrams(string):
    strArry = string.split(" ")
    stringList2 = list(itertools.combinations(strArry,2))
    count = 0
    searched =[]
    #print(stringList2)
    
    for x in stringList2:
        #print(x)
        if x[0] == x[1]:
            continue
        permlist = itertools.permutations(x[1])
        string_list =  map(''.join, permlist)
        #print(x[0])
        #print(string_list)
        if x[0] in string_list and x[0] not in searched:
            searched.append(x[0])
            #print(x[0])
            #print(string_list)
            
            
            count +=1
        
            #count +=1
    
    #print(stringList2)
    #print(list("".join(itertools.permutations(stringList2[0][1]))))
    #permlist = itertools.permutations(stringList2[0][1])
    #string_list =  map(' '.join, permlist) 
    #print(string_list)
    return count



print(CountingAnagrams("aa aa odg dog gdo"))
    