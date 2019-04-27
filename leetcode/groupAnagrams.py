def groupAnagrams(strs):
    groupHashMap = {}
    
    for x in strs:
        groupHash = list(map(hash,tuple(x)))
        print(groupHash)
        
        if sum(groupHash) not in groupHashMap:
            groupHashMap[sum(groupHash)] = []
            groupHashMap[sum(groupHash)].append(x)
        elif sum(groupHash) in groupHashMap:
            groupHashMap[sum(groupHash)].append(x)
    
    
    print(groupHashMap)
    
    finalArr = []
    
    for vals in groupHashMap.values():
        finalArr.append(vals)
    
    return finalArr



print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
            
        