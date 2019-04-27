import itertools

test = [5, 2, 1, 9, 50, 56]

test2 =  list(itertools.permutations(test))
#print(test2)

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

print(temp)