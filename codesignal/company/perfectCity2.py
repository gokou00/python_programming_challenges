#https://stackoverflow.com/questions/36586469/find-distance-between-2-points-on-grid
import math
def perfectCity(departure,destination):
    fracx1,wholex1 = math.modf(departure[0])
    fracx2,wholex2 = math.modf(destination[0])
    
    if wholex1 != departure[0] and wholex2 != destination[0] and wholex1 == wholex2:
        x = min(fracx1 + fracx2, (1-fracx1) + (1-fracx2))
        return abs(departure[1] - destination[1]) + x
        
    fracy1,wholey1 = math.modf(departure[1])
    fracy2,wholey2 = math.modf(destination[1])
    
    if wholey1 != departure[1] and wholey2 != destination[1] and wholey1 == wholey2:
        y = min(fracy1 + fracy2, (1-fracy1) + (1-fracy2))
        return abs(departure[0] - destination[0]) + y
    
    return abs(departure[0] - destination[0]) + abs(departure[1] - destination[1])
    
    

print(perfectCity([0, 0.4],[1, 0.6]))