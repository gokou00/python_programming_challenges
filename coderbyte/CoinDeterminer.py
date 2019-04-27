def CoinDeterminer(num):
    count = 0
    
    numCoins = []
    
    temp = num
    
    CoinDem = [11,9,7,5,1]
    totalCoins = 0
    
    while CoinDem:
        
        for x in CoinDem:
            if temp // x == 0:
                continue
            totalCoins += temp // x
            temp %= x
            
        
        temp = num
        numCoins.append(totalCoins)
        totalCoins = 0
        CoinDem.pop(0)
    
    numCoins.sort()
    #print(numCoins)
    return numCoins[0]




print(CoinDeterminer(14))
            
            
    
    
    