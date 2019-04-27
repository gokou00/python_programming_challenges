def two_sum(numbers, target):
    finalAns = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if numbers[i] + numbers[j] == target:
                finalAns.append(i)
                finalAns.append(j)
                return finalAns




print(two_sum([2,2,3], 4))