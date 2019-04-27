def findRepeatedDnaSequences(s):
    testMap1 = {}
    testMap2 = {}
    
    print(hash(("t","r","y")))
    print(hash(("r","t","y")))
    
    finalAns = []
    
    for i in range(len(s)):
        print(s[i:i+10])
        testMap1[hash(s[i:i+10])] = s[i:i+10]
        if hash(s[i:i+10]) not in testMap2:
            testMap2[hash(s[i:i+10])] = 1
        else:
            testMap2[hash(s[i:i+10])]+=1
        
        
        if testMap2[hash(s[i:i+10])] > 1 and testMap1[hash(s[i:i+10])] not in finalAns:
            finalAns.append(testMap1[hash(s[i:i+10])])
    
    
    #print(testMap1)
    #print(testMap2)
    return finalAns




print(findRepeatedDnaSequences("AAAAAAAAAAAA"))



            