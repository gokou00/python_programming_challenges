import itertools
def ParallelSums(arr):
    if sum(arr) % 2 != 0:
        return -1
    
    ans = sum(arr) / 2
    length = len(arr) / 2
    
    
    arr.sort()
    for L in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, L):
            if sum(subset) == ans and len(subset) == length:
                break
        
        if sum(subset) == ans and len(subset) == length:
            break
    
    #print(list(subset))
    
    subset1 = list(subset)
    #print(subset1)
    subset2 = []
    
    for x in subset1:
        idx = arr.index(x)
        del arr[idx]
    
    subset2 = arr[:]
    
    #print(subset1)
    #print(subset2)
    
    subset1.sort()
    subset2.sort()
    
    strbuild = ""
    
    if subset1[0] < subset2[0]:
        for x in subset1:
            strbuild += str(x)
            strbuild +=","
        for x in subset2:
            strbuild += str(x)
            strbuild += ","
            
        temp = list(strbuild)
        del temp[-1]
        strbuild = "".join(temp)
        return strbuild
        
    else: 
        for x in subset2:
            strbuild += str(x)
            strbuild +=","
        for x in subset1:
            strbuild += str(x)
            strbuild += ","
            
        temp = list(strbuild)
        del temp[-1]
        strbuild = "".join(temp)
        return strbuild
        
    


print(ParallelSums([1,1,1,1]))
            
            
        