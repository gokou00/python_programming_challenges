import itertools
def MatchingCouples(arr):
    a = [1,2,3,4,5,6,7,8,9,10]
    b = [1,2,3,4,5]
    dictMact = {}
    
    test = list(itertools.combinations(itertools.chain(a,b), 4))
    
    for i in test:
        dictMact[i] = 0

    
    
    print(len(test))
    print(len(dictMact))



print(MatchingCouples([55,55]))