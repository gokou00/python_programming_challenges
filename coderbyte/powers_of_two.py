# using the  sqrt function to complete
import math

def PowersofTwo(num):
    ans = math.sqrt(num)
    frac,whole = math.modf(ans)
    
    if frac == 0.0:
        return True
    else:
        return False
        

print(PowersofTwo(124))
    