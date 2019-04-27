def sockMerchant(n, ar):
    matchpair = {}
    #matchpair[-9999999]=0
    count = 0
    
    for x in ar:
        #matchpair[x]
        if x not in matchpair:
            matchpair[x] = 1
        else:
            matchpair[x] += 1
    
    #print(matchpair)
    
    
    for x in matchpair:
        if matchpair[x] >= 2:
            count += matchpair[x] // 2
    
    
    return count



print(sockMerchant(7,[1,2,1,2,1,3,2]))
    