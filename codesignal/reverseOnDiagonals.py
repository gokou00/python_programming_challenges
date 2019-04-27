def reverseOnDiagonals(matrix):
    i = 0
    j = len(matrix)
    
    while(i<j):
        matrix[i][i], matrix[j-1][j-1] = matrix[j-1][j-1],matrix[i][i]
        matrix[i][j-1],matrix[j-1][i] = matrix[j-1][i],matrix[i][j-1]
        i += 1
        j -= 1
    
    return matrix
    


print(reverseOnDiagonals([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))