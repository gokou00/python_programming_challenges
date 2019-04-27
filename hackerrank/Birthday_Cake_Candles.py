def birthdayCakeCandles(ar):
    ar.sort()
    return ar.count(ar[len(ar)-1])



print(birthdayCakeCandles([3, 2, 1 ,3]))