from collections import OrderedDict
def howManySundays(n, startDay):
    count = 0
    days_of_week = OrderedDict()
    days_of_week[1] = "Sunday"
    days_of_week[2] = "Monday"
    days_of_week[3] = "Tuesday"
    days_of_week[4] = "Wednesday"
    days_of_week[5] = "Thursday"
    days_of_week[6] = "Friday"
    days_of_week[7] = "Saturday"
    
    
    nums_days_week = OrderedDict()
    nums_days_week["Sunday"] = 1
    nums_days_week["Monday"] = 2
    nums_days_week["Tuesday"] = 3
    nums_days_week["Wednesday"] = 4
    nums_days_week["Thursday"] = 5
    nums_days_week["Friday"] = 6
    nums_days_week["Saturday"] = 7
    
    start = nums_days_week[startDay]
    if start == 7:
        start = 1
    else:
        start += 1
    
    
    for i in range(n):
        if days_of_week[start] == "Saturday":
            start = 1
            continue
        elif days_of_week[start] == "Sunday":
            count += 1
        
        start += 1
    
    return count

print(howManySundays(3,"Wednesday"))
        
    