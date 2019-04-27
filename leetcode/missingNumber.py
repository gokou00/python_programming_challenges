def missingNumber(nums):
    length = len(nums) +1
        
        #setNums = set(nums)
        
        #if len(nums) == 1 and nums[0] == 0:
            #return 1
        #elif len(nums) == 1 and nums[0] == 1:
            #return 0
            
    split = length // 2
        
        

        
        #start = nums[0]
        
    for i in range(0,split):
        if i not in set(nums):
            return i
        
    for i in range(0,split+1):
        if i not in set(nums):
            return i 