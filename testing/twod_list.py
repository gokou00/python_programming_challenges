# https://stackoverflow.com/questions/44111225/how-to-get-all-sub-matrices-of-2d-array-without-numpy
def VowelSquare(strArr):
    for i in range(len(strArr)):
        for j in range(len(strArr[0])):
            
            for t in range(i,i+2):
                for u in range(j, j +2):
                    print(strArr[i][j])



print(VowelSquare(["abcd", "eikr", "oufj"]))
    