def numberAndIPaddress(s):
    # coding and coding..
    ip_array = s.split(".")
    arr = []
    count = 0
    ipbuild = ""
    
    if len(ip_array) == 1:
        dec = str(int(bin(int(s))[2:]))
        #dec = int(s)
        #dec2 = format(dec,"#010b")
        
        print(dec)
        
        dec = dec[::-1]
        
        for x in dec:
            if count == 8:
                arr.append(ipbuild)
                count = 1
                ipbuild = x
                continue
            else:
                ipbuild += x
                count+=1
        
        #if ipbuild
        arr.append(ipbuild)
        print(arr)
        print(ipbuild)
        test = arr[0]
        print(int(test,2))
        
        return
        
    print(ip_array)
    bin_array = []
    for x in ip_array:
        temp = int(x)
        bin_array.append(bin(temp)[2:])
    print(bin_array)
    bin_array2 = []
    for x in bin_array:
        if len(x) != 8:
            temp = "0" * (8 - len(x))
            temp2 = temp + x
            bin_array2.append(temp2)
        else:
            bin_array2.append(x)
    print(bin_array2)
    bin_join = "".join(bin_array2)
    print(bin_join)
    print(int(bin_join,2))
    #pass
    return str(int(bin_join,2))
    
numberAndIPaddress('167969729')