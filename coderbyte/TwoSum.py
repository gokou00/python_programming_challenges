def TwoSum(arr):
    ans = arr.pop(0)
    arr_final = []
    stringbuild = ""
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == ans:
                arr_final.append(arr[i])
                arr_final.append(arr[j])
                stringbuild += str(arr[i])
                stringbuild += ","
                stringbuild += str(arr[j])
                stringbuild += " "
    
    if len(arr_final) == 0:
        return -1
    else:
        return stringbuild
        
print(TwoSum([7, 3, 5, 2, -4, 8, 11]))