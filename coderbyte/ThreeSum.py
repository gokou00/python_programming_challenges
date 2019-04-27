import itertools
def ThreeSum(arr):
    ans = arr.pop(0)
    
    for L in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, L):
            if len(subset) == 3 and sum(subset) == ans:
                print(subset)
                return "true"
    
    return "false"




print(ThreeSum([5, -6, 4, -5, -3, -2, 7, 1, 2, 12, 8, 14]))
