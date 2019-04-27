import itertools
def PrimeChecker(num):
    prime = []
    prime.append(2)
    prime.append(3)
    isPrime = True
    
    # generate list of primes
    for i in range(4,1000):
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        
        if isPrime:
            prime.append(i)
        else:
            isPrime = True
        #prime.append(i)
    
    
    #print(prime)
    
    
    numStr = str(num)
    numStrList = list(numStr)
    
    perm = list(itertools.permutations(numStrList))
    
    for x in perm:
        temp = "".join(x)
        tempNum = int(temp)
        if tempNum in prime:
            return 1
    
    return 0    


print(PrimeChecker(598))