def crossingSum(matrix, a, b):
    total = 0
    arr = []
    for idx,val in enumerate(matrix):
        if idx == a:
            arr = arr + val
            
    #print(arr)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == a and j == b:
                continue
            if j == b :
                arr.append(matrix[i][j])
    
  
    return sum(arr)



print(crossingSum([[100]] ,0,0))
    