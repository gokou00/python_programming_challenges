def PrimeTime(num):
    #isPrime = False
    
    for i in range(2,num):
        if num % i == 0:
            return "false"
    
    return "true"
    
print(PrimeTime(2))