def DashInsert(string):
    buildStr = ""
    for i in range(0,len(string) -1):
        if int(string[i]) % 2 == 1 and int(string[i+1]) % 2 == 1:
            buildStr += string[i] + "-"
        else:
            buildStr += string[i]
            
    buildStr += string[len(string)-1]
    print(buildStr)
    
    
DashInsert("454793")
    