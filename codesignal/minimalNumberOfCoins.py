def minimalNumberOfCoins(coins, price):
    numCoins = 0
    
    for x in coins[::-1]:
        if price // x != 0:
            numCoins+= price // x
            price %= x
    
    
    return numCoins



print(minimalNumberOfCoins([1, 2, 10],28))
            