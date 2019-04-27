def OffLineMinimum(strArr):
    numArray = []
    finsh = []
    final_str = ""
    
    for x in strArr:
        if x == "E":
            finsh.append(str(numArray.pop(0)))
        elif x != "E":
            temp = int(x)
            numArray.append(x)
            numArray.sort()
            
    
    print(finsh)
    for x in finsh:
        final_str += x
        final_str += ","
    
    final_str = final_str[:len(final_str)-1]
    return final_str
    
    

print(OffLineMinimum(["5","4","6","E","1","7","E","E","3","2"]))
            