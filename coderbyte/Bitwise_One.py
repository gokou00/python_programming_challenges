def BitwiseOne(strArr):
    bin1 = strArr[0]
    bin2 = strArr[1]
    
    final = ""
    
    for i in range(len(bin1)):
        if bin1[i] == "1" or bin2[i] == "1":
            final += "1"
        else:
            final += "0"
    
    #print(final)
    return final

print(BitwiseOne(["00011", "01010"]))    

