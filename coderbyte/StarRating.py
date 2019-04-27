import math
def StarRating(string):
    num = float(string)
    ratingRev = ["empty","empty","empty","empty","empty"]
    
    if string == "0.0":
        finalStr = " ".join(ratingRev)
        return finalStr
        
    
    frac,whole = math.modf(num)
    if whole == 0.0 and frac > 0.0:
        ratingRev[0] = "half"
        finalStr = " ".join(ratingRev)
        return finalStr
    
    
    if frac <= 0.1 and whole > 0.0:
        for i in range(int(whole)):
            ratingRev[i] = "full"
        
        finalStr = " ".join(ratingRev)
        return finalStr
    
    if frac >= 0.51 and whole > 0.0:
        for i in range(int(whole)):
            ratingRev[i] = "full"
        
        ratingRev[int(whole)] = "full"
        finalStr = " ".join(ratingRev)
        return finalStr
    
    
    if frac > 0.0 and whole > 0.0:
        for i in range(int(whole)):
            ratingRev[i] = "full"
        
        ratingRev[int(whole)] = "half" 
        
        finalStr = " ".join(ratingRev)
        return finalStr
    
    


print(StarRating("2.75"))
    
    
    
    
    
    