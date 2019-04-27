import math

def loose_change(cents):
    
    change_dict = {}
    change_dict['Quarters'] = 0
    change_dict['Dimes'] = 0
    change_dict['Pennies'] = 0
    change_dict['Nickels'] = 0
    
    if cents <= 0:
        return change_dict
    
    frac,whole = math.modf(cents)
    
    cents = whole
    
    
    if cents // 25 != 0:
        change_dict['Quarters'] = int(cents // 25) 
        cents = cents % 25
    
    if cents // 10 != 0:
        change_dict['Dimes'] = int(cents // 10) 
        cents = cents % 10
    
    if cents // 5 != 0:
        change_dict['Nickels'] = int(cents // 5) 
        cents = cents % 5
    
    if cents // 1 != 0:
        change_dict['Pennies'] = int(cents // 1) 
        cents = cents % 1
    
    
    
    
    
    return change_dict
    
print(loose_change(3.9))