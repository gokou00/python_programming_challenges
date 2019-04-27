import itertools
def largest_arrangement(numbers):
    test2 =  list(itertools.permutations(numbers))
    strBuilder = ""
    temp = 0 
    strNum = 0
    for x in test2:
        l = list(x)
        for j in l:
            strBuilder += str(j)
        strNum = int(strBuilder)
        strBuilder = ""
        if strNum > temp:
            temp = strNum
            
    return temp

print(largest_arrangement([5, 2, 1, 9, 50, 56]))
    