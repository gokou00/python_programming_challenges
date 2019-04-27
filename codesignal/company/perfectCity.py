import math
def perfectCity(departure,destination):
    x1 = departure[0]
    x2 = destination[0]
    y1 = departure[1]
    y2 = destination[1]
    
    # could be three options 
    # if either x1 or x2 or y1 or y2 are whole numbers use the taxicab distance
    # if x1 and x2 are dec or y1 and y1 are dec find the 
    
    fractotal = 0.0
    
    for x in departure:
        frac,whole = math.modf(x)
        if frac > 0:
            fractotal += (1-frac)
            
    for x in destination:
        frac,whole = math.modf(x)
        if frac > 0:
            fractotal += (1-frac)
    
    print(fractotal)
    
    
    temp1 = round(math.pow(x2-x1,2),3) 
    temp2 = round(math.pow(y2-y1,2),3)
    
    testfrac,testwhole = math.modf(5)
    print(testfrac)
    print(testwhole)
    
    total = temp1 + temp2
    #have to brute force. it depends on how many decimals you have for ex. 2.4 could be .6 to make it 3 or .4 to make it 2 
    
    
    return round(math.sqrt(total)) #+ fractotal # have to factor that you can't ride through the blocks can only go on streets. if the numbers are factions have to get to a whole number 


print(perfectCity([0, 0.2],[7, 0.5]))
    