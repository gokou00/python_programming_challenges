def matrixfy(st):
    perfect_sqaure = {1:1,4:2,9:3,16:4,25:5,36:6,49:7,64:8,81:9,100:10}
    print(perfect_sqaure)
    num_rows = 0
    matrix = []
    count = 0
    
    if len(st) == 0:
        return "name must be at least one letter"
    
    sqaure_keys = list(perfect_sqaure.keys())
    sqaure_keys.sort()
    
    
    if len(st) in sqaure_keys:
        num_rows = perfect_sqaure[len(st)]
        matrix = [[] for i in range(num_rows)]
        
    else:
        for x in sqaure_keys:
            if(x > len(st)):
                num_rows = perfect_sqaure[x]
                matrix = [[] for i in range(num_rows)]
                break
    for i in range(0,num_rows):
        for j in range(0,num_rows):
            if count < len(st):
                matrix[i].append(st[count])
                count+=1
            else:
                matrix[i].append(".")
    
        
    print(matrix)
    
    
    
    
matrixfy("Franklin")

    