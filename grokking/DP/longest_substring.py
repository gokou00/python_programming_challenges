def longestSubString(string1,string2):
    string1Array = list(string1)
    string2Array = list(string2)
    matrix = []
    
    # creating a 2d list. the val in range is the number of rows and the val in the for loop are the cols.
    for i in range(len(string1)):
        matrix.append([0] * len(string2))
    

    for i in range(len(string1Array)):
        for j in range(len(string2Array)):
            if string1Array[i]  == string2Array[j]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = 0
        
    
    print(max(matrix))
    


print(longestSubString("hish","vista"))
