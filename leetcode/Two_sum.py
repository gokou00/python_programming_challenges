#import random
def twoSum(nums, target):
    finalArr = []
    
    #finalArr = []
        
    for x in range(len(nums)):
        temp = target - nums[x]
        #print(temp)
        if temp in nums[x+1:]:
            print(temp)
            
            idx = nums.index(temp)
            if idx == x:
                idx = nums[::-1].index(temp)
                idx = (len(nums) -1) - idx
            return [x,idx]
            
 
    
    
  


print(twoSum([2,5,5,11],10))
