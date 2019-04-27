def fareEstimator(ride_time,ride_distance,cost_per_minute,cost_per_mile):
    finalArr = []
    
    for i in range(len(cost_per_mile)):
        temp = cost_per_minute[i] * ride_time + cost_per_mile[i] * ride_distance
        temp = round(temp,2)
        finalArr.append(temp)
    
    

    
    return finalArr


print(fareEstimator(30,7,[.2, .35, .4, .45],[1.1, 1.8, 2.3, 3.5]))