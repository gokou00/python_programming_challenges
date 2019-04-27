def electionsWinners(votes, k):
    
    count = 0
    isGreater = True
    votes.sort()
    largest = votes[-1]
    tracker = 0
    
    if votes[-1] != votes[-2]:
        count +=1
    
    for (i,val1) in enumerate(votes):
        temp = val1 + k 

        if temp > largest:
            count+=1
            tracker += 1

    return count
    
print(electionsWinners([5, 1, 3, 4, 1],0))