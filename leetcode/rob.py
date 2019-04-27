def rob(nums):
    totaleven = 0
    totalodd = 0
    
    idx = 0
    total = 0
    
    for i,val in enumerate(nums):
        total = val
        idx = i
        for j,val2 in enumerate(nums):
            if i == j:
                continue
            

    
    
    #print(totaleven)
    #print(totalodd)
    
    
    if totaleven >= totalodd:
        return totaleven
    else:
        return totalodd
    
    
print(rob( [2,1,1,2] ))