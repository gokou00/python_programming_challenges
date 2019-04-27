def TimeConvert(num):
    #num should be in minutes
    hours = num // 60
    mins = num % 60
    
    finaltime = str(hours) + ":" + str(mins)

    # code goes here 
    return finaltime


print(TimeConvert(45))