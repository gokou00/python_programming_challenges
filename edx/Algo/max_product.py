def MaxProduct(num):
    largest = 0
    numstr = str(num)
    
    for i in range(len(numstr)):
        for j in range(len(numstr)):
            if numstr[i] == numstr[j]:
                continue
            else:
                temp = int(numstr[i]) * int(numstr[j])
                if temp > largest:
                    largest = temp
    
    return largest


print(MaxProduct(58754485452455456545454556))
