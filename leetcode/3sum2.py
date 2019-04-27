#just like 2 sum for will have to first try with a nest for loop
#use a set to get all the unique answers

def threeSum(nums):
    nums.sort()
    finalArr = []
    #hashnum = 0
    #hashList = []
    testSet = set()
    
    for i in range(len(nums)-2):
        a = nums[i]
        start = i+ 1
        end = len(nums) - 1
        while (start < end):
            b = nums[start]
            c = nums[end]
            #hashnum = hash(a) + hash(b) + hash(c)
            
            if a+b+c == 0:
                #hashList.append(hashnum)
                finalArr.append([a,b,c])
                testSet.add([a,b,c])
                start += 1
                end -=1
            elif a+b+c > 0:
                end-=1
            else:
                start +=1
    
    print(testSet)
    print(finalArr)
    return testSet
                
    



print(threeSum(   [-1,0,1,2,-1,-4]    ))