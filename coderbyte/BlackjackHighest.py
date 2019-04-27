def BlackjackHighest(strArr):
    deck = {}
    deck["two"] = 2
    deck["three"] = 3
    deck["four"] = 4
    deck["five"] = 5
    deck["six"] = 6
    deck["seven"] = 7
    deck["eight"] = 8
    deck["nine"] = 9
    deck["ten"] = 10
    deck["jack"] =10
    deck["queen"] = 10
    deck["king"] = 10
    hasAce = False
    rank = {}
    rank["two"] = 2
    rank["three"] = 3
    rank["four"] = 4
    rank["five"] = 5
    rank["six"] = 6
    rank["seven"] = 7
    rank["eight"] = 8
    rank["nine"] = 9
    rank["ten"] = 10
    rank["jack"] = 11
    rank["queen"] = 12
    rank["king"] = 13
    total = 0
    highestCard = ""
    highestNum = 0
    
    
    if "ace" in strArr:
        hasAce = True
        idx = strArr.index("ace")
        del strArr[idx]
    
    if hasAce:
        for x in strArr:
            total += deck[x]
        
        if total + 11 > 21:
            deck["ace"] = 1
            rank["ace"] = 1
            strArr.append("ace")
        else:
            deck["ace"] = 11
            rank["ace"] = 14
            strArr.append("ace")
    
    #find highest card 
    
    for x in strArr:
        if rank[x] > highestNum:
            highestNum = rank[x]
            highestCard = x
    
    print(highestCard)
    total = 0
    
    for x in strArr:
        total += deck[x]
    
    if total == 21:
        return "blackjack " + highestCard
    elif total > 21:
        return "above " + highestCard
    else:
        return "below " + highestCard

print(BlackjackHighest(["two","three","four","five","six","ace"]))
    