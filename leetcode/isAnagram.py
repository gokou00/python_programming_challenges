def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    hash1 = 0
    hash2 = 0
    
    
    for i in range(len(s)):
        hash1 += hash(s[i])
        hash2 += hash(t[i])
    
    
    print(hash1)
    print(hash2)
    
    
    
    
    
    return hash1 == hash2




print(isAnagram("ac","bb"))
        