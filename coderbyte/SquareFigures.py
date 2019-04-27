def SquareFigures(num):
    squrt = 1
    squrtStr = ""
    count = 1
    
    if num == 1:
        return 0
    
    while len(squrtStr) < num:
        squrt = count ** 2
        squrtStr = str(squrt)
        count += 1
    
    
    #print(squrt)
    return count -1 




print(SquareFigures(3))