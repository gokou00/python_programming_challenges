import math
def BasicRomanNumerals(string):
    romantable ={}
    romantable["I"] = 1
    romantable["V"] = 5
    romantable["X"] = 10
    romantable["L"] = 50
    romantable["C"] = 100
    romantable["D"] = 500
    romantable["M"] = 1000
    
    arr_table = []
    total = 0
    
    for x in string:
        arr_table.append(romantable[x])
        
    print(arr_table)
    
    #total += arr_table[0]
        
    for i in range(len(arr_table)-1,-1,-1):
        if len(arr_table) -1 == i:
            total += arr_table[i]
        elif arr_table[i] < arr_table[i+1]:
            total-=arr_table[i]
        else:
            total+= arr_table[i]
    

        

    
    #total += arr_table[-1]
    return total
    

print(BasicRomanNumerals("LXXXIX"))