# https://www.hackerrank.com/challenges/triple-sum/problem
import itertools
def threesum():
    a = [1,3,5,7]
    b = [5,7,9]
    c = [7,9,11,13]
    uni = {}
    com = []
    for x in a:
        com.append(x)
    
    for x in b:
        com.append(x)
    for x in c:
        com.append(x)
        
    for L in range(0, len(com)+1):
        for subset in itertools.combinations(com, L):
            if len(subset) == 3:
                #print(subset)
                #return "true"
                if subset[0] in a and subset[1] in b and subset[2] in c and subset[0] <= subset[1] and subset[1] >= subset[2]:
                    uni[subset] = 0
    
    print(uni)
    return len(uni)

print(threesum())