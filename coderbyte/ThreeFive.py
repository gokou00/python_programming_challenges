def ThreeFiveMultiples(num):
    storageArr = []
    
    for i in range(num):
        if i % 5 == 0:
            storageArr.append(i)
        elif i % 3 == 0:
            storageArr.append(i)
        
    return sum(storageArr)



print(ThreeFiveMultiples(1))