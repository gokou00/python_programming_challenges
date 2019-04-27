import itertools

def WaveSorting(arr):
    
    for x in list(itertools.permutations(arr)):
        if checker(list(x)) == True:
            print(x)
            return True
        else:
            continue
        
    
    
    
    return False
    
    
    
#Zig Zag checker

def checker(arr):
    count = 1
    for i in range(len(arr) - 1):
        if count % 2 == 1:
            if arr[i] > arr[i+1]:
                count+=1
                continue
                
            else:
                return False
        
        if count % 2 == 0:
            if arr[i] < arr[i+1]:
                count+=1
                continue
            else:
                return False
    
    return True
    

print(WaveSorting([1, 1, 1, 1, 5, 2, 5, 1, 1, 3, 5, 6, 8, 3]))
        