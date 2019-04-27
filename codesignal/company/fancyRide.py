def fancyRide(l, fares):
    arr = []
    
    for x in fares:
        arr.append(l * x)
    
    ans = {}
    ans[0] = "UberSUV"
    ans[1] = "UberBlack"
    ans[2] = "UberPlus"
    ans[3] = "UberXL"
    ans[4] = "UberX"
    count = 0
    
    for x in arr[::-1]:
        if 20 >= x:
            break
        
        count += 1
    return ans[count]
