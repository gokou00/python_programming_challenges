def electionsWinners(votes, k):
    
    count = 0
    isGreater = True
    
    for (i,val1) in enumerate(votes):
        temp = val1 + k
        for (j,val2) in enumerate(votes):
            if i == j:
                continue
            elif temp <= val2:
                isGreater = False
                break
        
        if isGreater:
            count+= 1
            #isGreater = True
        isGreater = True
    return count
    
print(electionsWinners([5, 1, 3, 4, 1],0))