import itertools
def ScaleBalancing(strArr):
    string1 = strArr[0]
    string2 = strArr[1]
    stringbuild = ""
    
    num_arrbalance = []
    num_array = []
    
    for x in string1:
        if x >= "0" and x <= "9":
            stringbuild += x
        elif stringbuild != "":
            num_arrbalance.append(int(stringbuild))
            stringbuild = ""
    
    if stringbuild != "":
        num_arrbalance.append(stringbuild)
    
    
    for x in string2:
        if x >= "0" and x <= "9":
            stringbuild += x
        elif stringbuild != "":
            num_array.append(int(stringbuild))
            stringbuild = ""
            
    
    if stringbuild != "":
        num_array.append(stringbuild)

    
    
    #print(num_arrbalance)
    #print(num_array)
    
    diff = 0
    
    num1 = num_arrbalance[0]
    num2 = num_arrbalance[1]
    
    #print(num1)
    #print(num2)
    
    #if num1 > num2:
        #diff = num1 - num2
    #elif num2 > num1:
        #diff = num2 - num1
    #print(diff)
    
    finalArr = []
    builder = ""
    
    
    for L in range(0, len(num_array)+1):
        for subset in itertools.combinations(num_array, L):
            if len(subset) == 1:
                if num1 + sum(subset) == num2 or num2 + sum(subset) == num1:
                    finalArr =  list(subset)
            elif len(subset) == 2:
                if (num1 + sum(subset) == num2) or (num2 + sum(subset) == num1) or (num1 + subset[0] == num2 + subset[1]) or (num2 + subset[0] == num1 + subset[1]):
                    finalArr = list(subset)
                    break
        if len(finalArr) != 0:
            break
        
        
    
    if len(finalArr) == 0:
        return "not possible"
    elif len(finalArr) == 1:
        return str(finalArr[0])
    elif len(finalArr) == 2:
        builder += str(finalArr[0])
        builder += ","
        builder += str(finalArr[1])
        return builder
                
                
    
    
    
    #substract smaller number from larger and find the set that adds to the substracted value.     
    

    # code goes here 
    #return "not possible"


print(ScaleBalancing( ["[13, 4]", "[1, 2, 3, 6, 14]"] ))