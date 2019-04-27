def searchRange(nums,target):
    if target not in nums:
        return[-1,-1]
    
    idx1 = nums.index(target)
    
    if target not in nums[idx1+1:]:
        return[idx,-1]
    
    idx2 = nums[::-1].index(target)
    return[idx1,(len(nums) -1) - idx2]
    
print(searchRange([5,7,7,8,8,10],6))