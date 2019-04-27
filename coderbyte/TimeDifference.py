import itertools
from datetime import datetime

def TimeDifference(strArr):
    store_times = []
    all_combine = list(itertools.combinations(strArr,2))
    
    for x in all_combine:
        store_times.append(times(x[0],x[1]))
        store_times.append(times(x[1],x[0]))
    
    #print(store_times)
    
    store_times.sort()
    
    return store_times.pop(0)
    
    





def times(string1,string2):
    total_minutes = 0
    FMT = "%I:%M%p"
    tdelta = datetime.strptime(string2, FMT) - datetime.strptime(string1, FMT)
    #print(str(tdelta), " tdelta")
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
    
print(TimeDifference(["11:45pm", "11:45am"]))
            
            
        
    
    
    