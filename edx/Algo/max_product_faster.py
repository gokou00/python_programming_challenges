def MaxProduct(num):
    largest = 0
    numstr = str(num)
    print(len(num))
    
    if len(numstr) < 2:
        return num
    
    strArry = list(numstr)
    
    numArry = []
    
    for x in strArry:
        numArry.append(int(x))
    
    numArry.sort()
    
    return numArry[-1] * numArry[-2]


print(MaxProduct(9223372036854775808))
