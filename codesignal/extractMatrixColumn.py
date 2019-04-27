def extractMatrixColumn(matrix, column):
    arr = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == column:
                arr.append(matrix[i][j])
    
    
    
    return arr
    
    
    
print(extractMatrixColumn([[1,1],[5,0],[2,3]] ,0))