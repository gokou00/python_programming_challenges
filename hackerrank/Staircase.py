def staircase(n):
    staircaseArr = []
    
    stairBuilder = "#" * n
    #stairBuilderList = list(stairBuilder)
    #stairBuilder = ""
    
    #for i in range(n,0,-1):
        #stairBuilder = "#" * i
        #staircaseArr.append(stairBuilder)
    
    for i in range(n):
        if i == 0:
            staircaseArr.append(stairBuilder)
            tempList = list(stairBuilder)
            tempList[i] = " "
            stairBuilder = "".join(tempList)
            continue
        staircaseArr.append(stairBuilder)
        tempList = list(stairBuilder)
        tempList[i] = " "
        stairBuilder = "".join(tempList)
        
        #print(stairBuilder)
    
    
    
    #print(staircaseArr)
    #print(staircaseArr)
    
    for i in range(len(staircaseArr)-1,-1,-1):
        print(staircaseArr[i])
    
    





print(staircase(100))
        
    