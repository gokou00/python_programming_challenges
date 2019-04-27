def PrimeMover(num):
    prime = {}
    prime[1] = 2
    prime[2] = 3
    
    
    if num == 1:
        return 2
        
    if num == 2:
        return 3
    count = 2    
        
    isPrime = True
    
    for i in range(3,10001):
        for j in range(2,i):
            #print(i,j)
            if i % j == 0:
                #print(i,j)
                isPrime = False
                break
                
        #print(isPrime)
        if isPrime and count == num:
            return i
            
        if isPrime:
            count +=1
            #isPrime = True
        else:
            isPrime = True
            
        
        
   

            
        
        
    temp = prime[num]
    return temp

print(PrimeMover(400))