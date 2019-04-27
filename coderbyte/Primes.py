def Primes(num):
    
    if num == 1:
        return False
    
    if num == 2:
        return True
    
    
    isPrimes = True
    
    for i in range(2,num):
        if num % i == 0:
            isPrimes = False
            break
        
    
    return isPrimes


print(Primes(4))