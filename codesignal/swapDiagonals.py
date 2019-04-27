def swapDiagonals(matrix):
    i = 0
    j = len(matrix)
    
    for i in range(j):
        matrix[i][i], matrix[i][j-i - 1] = matrix[i][j-i-1],matrix[i][i]
        
        #matrix[i][i], matrix[j-1][j-1] = matrix[j-1][j-1],matrix[i][i]
        #matrix[i][j-1],matrix[j-1][i] = matrix[j-1][i],matrix[i][j-1]

    
    return matrix

 
print(swapDiagonals([[43,455,32,103], [102,988,298,981], [309,21,53,64], [2,22,35,291]]  ))