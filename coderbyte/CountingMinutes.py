from datetime import datetime
def CountingMinutes(string):
    stringArry = string.split("-")
    
    starttime = stringArry[0]
    endTime = stringArry[1]
    
    #print(starttime)
    #print(endTime)
    
    fmt = "%I:%M%p"
    
    start = datetime.strptime(starttime, fmt)
    end = datetime.strptime(endTime, fmt)
    
    diff =  end - start  
    #print(diff)
    
    minutes = diff.total_seconds() / 60
    
    #print(diff.total_seconds(), "test")
    
    total = 0
    
    if "-1 day" in str(diff):
        total = (24 * 60) - abs(minutes)
    else:
        total = int(minutes)
        
    
    
     
    
    
    
    #print(minutes)
    
    return int(total)



print(CountingMinutes("1:23am-1:08am"))
    
    
    