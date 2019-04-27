def findMedianSortedArrays(nums1, nums2):
    combinatedArr = nums1 + nums2
    #print(combinatedArr)
    
    sortedArr = sorted(combinatedArr)
    
    if len(sortedArr) % 2 != 0:
        idx = len(sortedArr) // 2
        
        return float(sortedArr[idx])
    
    idx = len(sortedArr) // 2
    #print(idx)
    
    return ((sortedArr[idx] + sortedArr[idx-1]) / float(2))
    


print(findMedianSortedArrays([1, 2],[3,4]))