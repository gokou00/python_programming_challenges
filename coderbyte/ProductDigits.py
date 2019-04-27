def ProductDigits(num):
    count = 0
    string1 = ""
    string2 = ""
    productArr = []
    
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i * j == num:
                #print(i)
                #print(j)
                count = len(str(i)) + len(str(j))
                productArr.append(count)
                #return count
    
    productArr.sort()
    return productArr[0]

print(ProductDigits(79))