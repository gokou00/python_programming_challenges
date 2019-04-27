def NumberSearch(string):
    numBuild = ""
    total = 0
    #str_num_array = []
    
    for x in string:
        if x >= "0" and x <= "9":
            numBuild += x
        elif numBuild != "":
            #str_num_array.append(numBuild)
            total += int(numBuild)
            numBuild = ""
    

    if numBuild != "":
        total += int(numBuild)
    return total
    
    
print(NumberSearch("3Hello 9"))