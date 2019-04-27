def mul_digits(num):
    total = 1
    pop = 0 
    
    while num != 0:
        pop = num % 10
        total *= pop
        num /= 10
    
    return total



def MultiplicativePersistence(num):
    count = 0
    total = num
    
    
    while total > 9:
        #print(total)
        
        total = mul_digits(total)
        #print(total)
        
        count += 1
    
        
        
    return count
    
print(MultiplicativePersistence(39))
    
    