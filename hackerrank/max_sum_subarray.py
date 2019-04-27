def maxSubarray(arr):
    subarray = []
    largest = 0
    for i in range(len(arr)):
        if i == 0:
            largest = arr[i]
            continue
        #subarray.append(max(arr[i], sum(arr[:i+1])))
        largest_end = max(arr[i],sum(arr[:i+1]))
        largest = max(largest_end,largest)
    #subarray.sort()
    print(largest)

print(maxSubarray([-1,2,3]))
