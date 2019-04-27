#use sets
#https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/

def OverlappingRanges(arr):
    limit = arr[len(arr) -1]
    first_range = []
    second_range = []
    first_end = arr[1]
    second_end = arr[3]
    
    for i in range(arr[0],first_end + 1):
        first_range.append(i)
    
    #print(first_range)
    
    for i in range(arr[2], second_end + 1):
        second_range.append(i)
        
    #print(second_range)
    
    first_set = set(first_range)
    second_set = set(second_range)
    
    intersec = first_set & second_set
    
    #print(len(intersec))
    
    if len(intersec) >= limit:
        return "true"
    else:
        return "false"
    


print(OverlappingRanges([1,8,2,4,4]))