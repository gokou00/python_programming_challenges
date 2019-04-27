def add_digits(num):
    total = 0
    pop = 0 
    
    while num != 0:
        pop = num % 10
        total += pop
        num /= 10
    
    return total



def AdditivePersistence(num):
    
    count = 0
    total = num
    
    
    while total > 9:
        
        total = add_digits(total)
        
        count += 1
    
        
        
    return count
    
    
        

print(AdditivePersistence(2718))
        
        
        
        