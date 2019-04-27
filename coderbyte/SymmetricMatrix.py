# https://stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy
def SymmetricMatrix(strArr):
    test1 = "".join(strArr)
    test2 = test1.split("<>")
    print(test2)
    print(len(test2))
    

print(SymmetricMatrix(["1","0","1","<>","0","1","0","<>","1","0","1"]))
    