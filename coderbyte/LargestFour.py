def LargestFour(arr):
    arr.sort()
    
    if len(arr) <= 4:
        return sum(arr)
    
    
    return sum(arr[-1:-5:-1])
    

print(LargestFour([1000045]))