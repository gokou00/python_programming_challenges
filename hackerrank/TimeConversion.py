def timeConversion(s):
    amORPM = s[-2:]
    hours = s[:2]
    intHours = int(hours)
    
    #print(amORPM)
    print(hours)
    strBuilder = ""
    minutes = s[3:5]
    seconds = s[6:8]
    
    print(minutes)
    print(seconds)
    
    militaryTime = {}
    militaryTime["01"] = "13"
    militaryTime["02"] = "14"
    militaryTime["03"] = "15"
    militaryTime["04"] = "16"
    militaryTime["05"] = "17"
    militaryTime["06"] = "18"
    militaryTime["07"] = "19"
    militaryTime["08"] = "20"
    militaryTime["09"] = "21"
    militaryTime["10"] = "22"
    militaryTime["11"] = "23"
    #militaryTime["05"] = "17"
    
    if hours == "12" and amORPM == "AM":
        return "00" + ":" + minutes + ":" + seconds
    
    if hours == "12" and amORPM == "PM":
        return "12" + ":" + minutes + ":" + seconds
    
    if amORPM == "AM":
        return hours + ":" + minutes + ":" + seconds
    
    if amORPM == "PM":
        return militaryTime[hours] + ":" + minutes + ":"+ seconds
    
    
    
    
    


print(timeConversion("07:05:45PM"))