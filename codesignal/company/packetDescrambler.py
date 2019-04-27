def packetDescrambler(seq,fragmentData,n):
    half = n /2.0
    #print(half)
    
    if 0 not in seq:
        return ""
    
    sortedSeq = sorted(seq)
    
    #seqStr = "".join(seq)
    #index = seq.index(sortedSeq[2])
    
    #print(index)
    strBuild = ""
    startidx = 0
    count = 0
    testmap ={}
    testmap[-1] = ""
    finalStr = ""
    testmap2map = {}
    testmap2map[-1] = True
    testmap3map = {}
    testmap3map[-1] = ""
    
    
    for i in range(len(sortedSeq)):
        
        if sortedSeq[i] not in testmap2map:
            testmap2map[sortedSeq[i]] = False
            
        indx = seq.index(sortedSeq[i])
        seq[indx] = -1
        strBuild += fragmentData[indx]
        
        #startidx +=1
        #print(sortedSeq[i])
        if sortedSeq[i] not in testmap:
            testmap[sortedSeq[i]] = ""
            testmap[sortedSeq[i]] += fragmentData[indx]
            
        else:
            testmap[sortedSeq[i]] += fragmentData[indx]
            
            
        if(testmap[sortedSeq[i]].count(fragmentData[indx]) > half) and sortedSeq[i] not in testmap3map :
            testmap3map[sortedSeq[i]] = ""
            
            
            
        if (testmap[sortedSeq[i]].count(fragmentData[indx]) > half) and (fragmentData[indx] not in testmap3map[sortedSeq[i]]):
            #finalStr += fragmentData[indx]
            #print(fragmentData[indx] ,testmap3map[sortedSeq[i]] )
            testmap2map[sortedSeq[i]] = True
            testmap3map[sortedSeq[i]] += fragmentData[indx]
            finalStr += testmap3map[sortedSeq[i]]
    
    
    

        
            
            

            
                
            
        
        
        
        
        
        
        
        
    
    print(testmap)
    print(finalStr)
    print(testmap2map)
    print(testmap3map)
    #checks to see if false is in testmap2 Gap test
    #checks if final has # as last char
    #checks to see if # is in any other pos
    #print(testmap2map.values())
    
    if False in testmap2map.values():
        return ""
    
    if "#" in finalStr[0:len(finalStr)-1]:
        print("test")
        return ""
    
    
    if "#" == finalStr[len(finalStr)-1]:
        return finalStr
    else:
        return ""
        
    






print(packetDescrambler([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3],["#", "?", "?", "?", "?", "?", "?", "?", "#", "?", "#", "#"],3))