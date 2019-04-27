def bingo(ticket,win):
    #print(len(ticket))
    matching_num = []
    
    ticket_array = []
    
    for i in range(len(ticket)):
        matching_num.append(ticket[i][1])
    
    
    print(matching_num)
    count_element = 0
    count = 0
    count_total = 0
    
    
    for i in range(len(ticket)):
        for x in ticket[i][0]:
            for char in x:
                ticket_array.append(ord(char))
            #print(ticket_array , "ticket array")
        print(ticket_array, "ticket array")
        print(matching_num[count], " matching_num")
        count_element = ticket_array.count(matching_num[count])
        #count += 1
        #print(matching_num[1])
        print(count_element , "count_element")
        if count_element > 0:
            count_total += 1
        count_element = 0
        ticket_array = []
        count += 1
        
    print(count_total)
    
    if count_total >= win:
        return "Winner!"
    else:
        return "Loser!"
            
    
    
    
    #print(matching_num)
    
    pass

print(bingo([['QQTKE', 65], ['UE', 66], ['FKPEL', 66], ['WIK', 85]],1))