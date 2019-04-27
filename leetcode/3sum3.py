#just like 2 sum for will have to first try with a nest for loop
#use a set to get all the unique answers
import hashlib
def threeSum(nums):
    answersets = set()
    hashlist = []
    answerList = []
    testDict = {}
    #nums.sort()
    #print(hash(str(-4))+ hash(str(2))+hash(str(2)))
    #print(hash(str(4))+ hash(str(-2))+ hash(str(-2)))
    
    #print([2,3,4]!=[2,3,4])
    #hash_object = hashlib.md5(b-4)
    #print(hash_object)
    
    
    
    for i,val in enumerate(nums):
        #target = nums.pop(i)
        #print(target)
        target = nums[i]
        nums[i] = -33333333333333334343434444444444443434343
        
        for j,val in enumerate(nums[i:]):
            #valTest = nums.pop(j)
            if i == j:
                continue
            
            valTest = nums[j]
            nums[j] = -344554545343433333333334545453445455454
            
            temp_sum = target + valTest
            
            target2 = 0 - temp_sum
            hash_object1 = hashlib.md5( str(target).encode() )
            hash_object2 = hashlib.md5( str(valTest).encode() ) 
            hash_object3 = hashlib.md5( str(target2).encode() ) 
            
            testHex = hash_object1.hexdigest() + hash_object2.hexdigest() + hash_object3.hexdigest()
            
            hashNum = hash(testHex)
            
            #print(target,valTest,target2)
            #hashNum = hash(str(target))  + hash(str(valTest))  + hash(str(target2)) 
            #hashNum /= (target+13) + (valTest+13) + (target2+13)
            #hashNum += random.randint(13,99)
            #print(hashNum)
            #print(hashlist)
            #if target2 in nums and hashNum not in hashlist:
            #if target2 in nums and testDict[hashNum] != [target,valTest,target2]:
            if target2 in nums[i:] and hashNum not in hashlist:
                answerList.append([target,valTest,target2])
                hashlist.append(hashNum)
                #answersets.add(tempArr)
                #hashNum = hash(str(target))  + hash(str(valTest))  + hash(str(target2))
                #hashlist.append(hashNum)
                #testDict[hashNum] = [target,valTest,target2]
                #if hashNum in hashlist and testDict[hashNum] != [target,valTest,target2]:
                    

                    
                    
                
                
                #answersets.add((target,valTest,target2))
            
            #nums.insert(j,valTest)
            nums[j] = valTest
        
        #nums.insert(i,target)
        nums[i] = target
    
    #testArr = {frozenset(x) for x in answerList}
    #print(testArr)
    
    #print(answersets)
    #print(answerList)
    #print(hashlist)
    #print(testDict)
    return answerList

print(threeSum(   [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]     ))