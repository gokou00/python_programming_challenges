#import itertools
def stringsCrossover(inputArray, result):
    count = 0
    

    for i in range(len(inputArray)):
        for j in range(i+ 1,len(inputArray)):

            word1 = inputArray[i]
            word2 = inputArray[j]
            #test = inputArray[i] + inputArray[j]
            #combinetest = set(list(map("".join, itertools.permutations(test,len(result)))))
            isCross = True
            for x in range(len(result)):
                if word1[x] != result[x] and word2[x] != result[x]:
                    isCross = False
                    break
            if isCross:
                count += 1 

                
    
    #print(testList)
    return count
            
    
    
    

print(stringsCrossover(["aaa", "aaa"] ,"aaa"))
                
    