def KaprekarsConstant(num):
    Kaprekars = 6174
    #print(list(num))
    str1 = ""
    str2 = ""
    
    count = 0
    
    while num != Kaprekars:
        str1 = str(num)
        if len(str1) < 4:
            str1 +="0"
        
        
        strArry = list(str1)
        aorder = sorted(strArry)
        dorder = sorted(strArry,reverse = True)
        anum = int("".join(aorder))
        dnum = int("".join(dorder))
        print(anum)
        print(dnum)
        
        if anum < dnum:
            num = dnum - anum
        elif anum > dnum:
            num = anum - dnum
        count += 1
        
        #if len(str(num)) < 4:
            
        
        print(num)
    
    return count
        
    



print(KaprekarsConstant(9831))