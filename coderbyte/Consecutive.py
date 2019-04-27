def Consecutive(arr):
    arr.sort()
    count = 0
    start = arr[0]
    end = arr[len(arr)-1]
    
    for i in range(start,end+1):
        if i not in arr:
            count += 1
    
    return count
    
print(Consecutive([-2,10,4]))