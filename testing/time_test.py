from datetime import datetime
def times(string1,string2):
    total_minutes = 0
    FMT = "%I:%M%p"
    tdelta = datetime.strptime(string2, FMT) - datetime.strptime(string1, FMT)
    if str(tdelta)[0] == "-":
        return 999999
    
    #idx = str(tdelta).index(":")
    
    time_array = str(tdelta).split(":")
    
    for i in range(len(time_array)):
        if i == 0:
            temp = int(time_array[i])
            h = temp * 60
            total_minutes += h
            continue
        elif i == 1:
            total_minutes += int(time_array[i])
    
    
    return total_minutes
            
            
        
    
    
    #hours = int(str(tdelta)[:idx])
    
    
    #print(str(tdelta)[2:])



print(times("1:30pm","2:10pm"))
    
    