def plusMinus(arr):
    posCount = 0
    negCount = 0
    zerCount = 0
    
    for x in arr:
        if x < 0:
            negCount += 1
        elif x > 0:
            posCount += 1
        elif x == 0:
            zerCount += 1
    posAns = round(float(posCount)/len(arr),6)
    negAns = round(float(negCount)/len(arr),6)
    zerAns = round(float(zerCount)/len(arr),6)
    
    
    print("%1.6f"  %(posAns))
    print("%1.6f"  %(negAns))
    print("%1.6f"  %(zerAns))


print(plusMinus([-4, 3, -9, 0, 4, 1]))