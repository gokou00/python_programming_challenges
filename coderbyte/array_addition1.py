import itertools
def ArrayAdditionI(arr):
    arr.sort()
    largest = arr[len(arr)-1]
    del arr[len(arr)-1]
    
    all_com = []
    
    #stuff = [1, 2, 3]
    for L in range(0, 5):
        for subset in itertools.combinations(arr, L):
            #print(list(subset))
            if sum(list(subset)) == largest:
                #print(True)
                return True
                
    return False

print(ArrayAdditionI([3,5,-1,8,12]))
    