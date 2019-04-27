import itertools

def possibleSums(coins, quantity):
    #print(list(itertools.combinations(coins, len(coins))))
    for L in range(0, len(coins)+1):
        for subset in itertools.combinations(coins, L):
            print(subset)
    
    
    

print(possibleSums([10, 50, 100],[1, 2, 1]))