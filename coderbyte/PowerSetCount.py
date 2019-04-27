import itertools
def PowerSetCount(arr):
    count = 0
    for L in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, L):
            #print(subset)
            count +=1
    
    return count


print(PowerSetCount([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    