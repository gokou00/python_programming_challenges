def countingValleys(n, s):
    seaLvl = 0
    walk = []
    numofValleys = 0
    inValley = False
    
    for x in s:
        if x == "U":
            seaLvl += 1
        if x == "D":
            seaLvl -= 1
        
        walk.append(seaLvl)
        #print(seaLvl)
    
    for x in walk:
        if x < 0 and inValley == False:
            inValley = True
            numofValleys += 1
        
        if x >= 0:
            inValley = False
            
    
    return numofValleys        


print(countingValleys(8,"DDUUUUDD"))

