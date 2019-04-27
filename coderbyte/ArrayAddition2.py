import itertools
def ArrayAddition(arr):
    sortedArr = sorted(arr)
    largest = sortedArr.pop()
    
    print(sortedArr)
    print(largest)
    
    for L in range(0,len(sortedArr)+1):
        for subset in itertools.combinations(sortedArr,L):
            if sum(subset) == largest:
                return "true"
    
    
    return "false"



print(ArrayAddition([1,2,3,4]))

