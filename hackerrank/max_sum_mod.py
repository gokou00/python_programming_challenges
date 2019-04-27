def maximumSum(a, m):
    dp_arr = []
    largest = 0
    for x in a:
        temp = x % m 
        if temp > largest:
            largest = temp
    
    for i in range(len(a)):
        #if i == 0:
            #dp_arr.append(a[i]%m)
            #largest = a[i]%m
            #continue
        sum_mod = sum(a[:i+i]) % m
        if sum_mod > largest:
            largest = sum_mod
        dp_arr.append(sum_mod)
    
    dp_arr.sort()
    
    #return dp_arr.pop()
    return largest

print(maximumSum([1, 2, 3],2))

        
    