from datetime import *
def CountingMinutesI(string):
    arraytime = string.split("-")
    #print(arraytime)
    start12 = arraytime[0][0:-2]
    start_period = arraytime[0][-2:]
    #print(start12)
    #start12 = start12 + " " + "am"
    
    if start_period == "pm":
        start12 = start12 + " " + "pm"
        start24 = datetime.strptime(start12, '%I:%M %p')
    elif start_period == "am":
        start12 = start12 + " " + "am"
        start24 = datetime.strptime(start12, '%I:%M %p')
        
    #print(start24)
    
    start24 = datetime.strftime(start24, "%H:%M")
    print(start24)
    
    
    end12 = arraytime[1][0:-2]
    end_period = arraytime[1][-2:]
    #end12 = end12 + " " + end_period
    #print(end12)
    #print(end_period)
    if end_period == "pm":
        end12 = end12 + " " + "pm"
        end24 = datetime.strptime(end12, '%I:%M %p')
    elif end_period == "am":
        end12 = end12 + " " + "am"
        end24 = datetime.strptime(end12, '%I:%M %p')
    
    #print(end24)
    
    end24 = datetime.strftime(end24, "%H:%M")
    
    
    print(end24)
    FMT = '%H:%M'
    tdelta = datetime.strptime(end24, FMT) - datetime.strptime(start24, FMT)
    #print(tdelta[-8:])
    
    test = str(tdelta)
    minutes = test[-8:]
    
    #print(test[-8:])
    
    minutesArray = minutes.split(":")
    
    total = 0
    total += int(minutesArray[0]) * 60
    total += int(minutesArray[1]) % 60
    
    print(total)
    
    
    #print(int(tdelta.total_seconds() / -60))
    
    #test = end24 - start24
    
    #print(test)
    #print(str(tdelta))
        
    
    
#CountingMinutesI("1:23am-1:08am")
#CountingMinutesI("12:30pm-12:00am")
CountingMinutesI("12:30pm-12:00am" )
