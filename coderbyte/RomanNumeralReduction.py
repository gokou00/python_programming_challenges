def RomanNumeralReduction(string):
    # first convert the roman numeral to an int
    #then use a greedy algo to reduce the letters
    romanAns = RomanNumeralInt(string)
    #print(romanAns)
    
    stringBuild = ""
    
    if romanAns / 1000 > 0:
        temp = romanAns / 1000
        stringBuild += "M" * temp
        romanAns = romanAns % 1000
    
    if romanAns / 500 > 0:
        temp = romanAns / 500
        stringBuild += "D" * temp
        romanAns = romanAns % 500
    
    if romanAns / 100 > 0:
        temp = romanAns / 100
        stringBuild += "C" * temp
        romanAns = romanAns % 100
        
    if romanAns / 50 > 0:
        temp = romanAns / 50
        stringBuild += "L" * temp
        romanAns = romanAns % 50
    
    if romanAns / 10 > 0:
        temp = romanAns / 10
        stringBuild += "X" * temp
        romanAns = romanAns % 10
    
    if romanAns / 5 > 0:
        temp = romanAns / 5
        stringBuild += "V" * temp
        romanAns = romanAns % 5
        
    if romanAns / 1 > 0:
        temp = romanAns / 1
        stringBuild += "I" * temp
        romanAns = romanAns % 1
    
    
    #print(stringBuild)
    return stringBuild
    
        
    

    
    
    


def RomanNumeralInt(string):
    roman = {}
    roman["I"] = 1
    roman["V"] = 5
    roman["X"] = 10
    roman["L"] = 50
    roman["C"] = 100
    roman["D"] = 500
    roman["M"] = 1000
    
    total = 0
    
    for i in range(len(string)-1,-1,-1):
        #print(i)
        if i == len(string) -1:
            total+= roman[string[i]]
            continue
        if roman[string[i]] < roman[string[i+1]]:
            total-= roman[string[i]]
            continue
        if roman[string[i]] >= roman[string[i+1]]:
            #temp = roman[string[i-1]]
            total += roman[string[i]]
            continue
    
    return total
        
        
        
        
print(RomanNumeralReduction("XXXVVIIIIIIIIII"))
    